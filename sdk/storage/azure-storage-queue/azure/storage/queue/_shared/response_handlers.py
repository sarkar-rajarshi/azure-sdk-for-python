# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import NoReturn
from xml.etree.ElementTree import Element

from azure.core.exceptions import (
    ClientAuthenticationError,
    DecodeError,
    HttpResponseError,
    ResourceExistsError,
    ResourceModifiedError,
    ResourceNotFoundError,
)
from azure.core.pipeline.policies import ContentDecodePolicy

from .authentication import AzureSigningError
from .models import get_enum_value, StorageErrorCode, UserDelegationKey
from .parser import _to_utc_datetime


SV_DOCS_URL = "https://learn.microsoft.com/rest/api/storageservices/versioning-for-the-azure-storage-services"
_LOGGER = logging.getLogger(__name__)


class PartialBatchErrorException(HttpResponseError):
    """There is a partial failure in batch operations.

    :param str message: The message of the exception.
    :param response: Server response to be deserialized.
    :param list parts: A list of the parts in multipart response.
    """

    def __init__(self, message, response, parts):
        self.parts = parts
        super(PartialBatchErrorException, self).__init__(message=message, response=response)


# Parses the blob length from the content range header: bytes 1-3/65537
def parse_length_from_content_range(content_range):
    if content_range is None:
        return None

    # First, split in space and take the second half: '1-3/65537'
    # Next, split on slash and take the second half: '65537'
    # Finally, convert to an int: 65537
    return int(content_range.split(" ", 1)[1].split("/", 1)[1])


def normalize_headers(headers):
    normalized = {}
    for key, value in headers.items():
        if key.startswith("x-ms-"):
            key = key[5:]
        normalized[key.lower().replace("-", "_")] = get_enum_value(value)
    return normalized


def deserialize_metadata(response, obj, headers):  # pylint: disable=unused-argument
    try:
        raw_metadata = {k: v for k, v in response.http_response.headers.items() if k.lower().startswith("x-ms-meta-")}
    except AttributeError:
        raw_metadata = {k: v for k, v in response.headers.items() if k.lower().startswith("x-ms-meta-")}
    return {k[10:]: v for k, v in raw_metadata.items()}


def return_response_headers(response, deserialized, response_headers):  # pylint: disable=unused-argument
    return normalize_headers(response_headers)


def return_headers_and_deserialized(response, deserialized, response_headers):  # pylint: disable=unused-argument
    return normalize_headers(response_headers), deserialized


def return_context_and_deserialized(response, deserialized, response_headers):  # pylint: disable=unused-argument
    return response.http_response.location_mode, deserialized


def return_raw_deserialized(response, *_):
    return response.http_response.location_mode, response.context[ContentDecodePolicy.CONTEXT_NAME]


def process_storage_error(storage_error) -> NoReturn:  # type: ignore [misc] # pylint:disable=too-many-statements, too-many-branches
    raise_error = HttpResponseError
    serialized = False
    if isinstance(storage_error, AzureSigningError):
        storage_error.message = (
            storage_error.message
            + ". This is likely due to an invalid shared key. Please check your shared key and try again."
        )
    if not storage_error.response or storage_error.response.status_code in [200, 204]:
        raise storage_error
    # If it is one of those three then it has been serialized prior by the generated layer.
    if isinstance(
        storage_error,
        (PartialBatchErrorException, ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError),
    ):
        serialized = True
    error_code = storage_error.response.headers.get("x-ms-error-code")
    error_message = storage_error.message
    additional_data = {}
    error_dict = {}
    try:
        error_body = ContentDecodePolicy.deserialize_from_http_generics(storage_error.response)
        try:
            if error_body is None or len(error_body) == 0:
                error_body = storage_error.response.reason
        except AttributeError:
            error_body = ""
        # If it is an XML response
        if isinstance(error_body, Element):
            error_dict = {child.tag.lower(): child.text for child in error_body}
        # If it is a JSON response
        elif isinstance(error_body, dict):
            error_dict = error_body.get("error", {})
        elif not error_code:
            _LOGGER.warning(
                "Unexpected return type %s from ContentDecodePolicy.deserialize_from_http_generics.", type(error_body)
            )
            error_dict = {"message": str(error_body)}

        # If we extracted from a Json or XML response
        # There is a chance error_dict is just a string
        if error_dict and isinstance(error_dict, dict):
            error_code = error_dict.get("code")
            error_message = error_dict.get("message")
            additional_data = {k: v for k, v in error_dict.items() if k not in {"code", "message"}}
    except DecodeError:
        pass

    try:
        # This check would be unnecessary if we have already serialized the error
        if error_code and not serialized:
            error_code = StorageErrorCode(error_code)
            if error_code in [StorageErrorCode.condition_not_met, StorageErrorCode.blob_overwritten]:
                raise_error = ResourceModifiedError
            if error_code in [StorageErrorCode.invalid_authentication_info, StorageErrorCode.authentication_failed]:
                raise_error = ClientAuthenticationError
            if error_code in [
                StorageErrorCode.resource_not_found,
                StorageErrorCode.cannot_verify_copy_source,
                StorageErrorCode.blob_not_found,
                StorageErrorCode.queue_not_found,
                StorageErrorCode.container_not_found,
                StorageErrorCode.parent_not_found,
                StorageErrorCode.share_not_found,
            ]:
                raise_error = ResourceNotFoundError
            if error_code in [
                StorageErrorCode.account_already_exists,
                StorageErrorCode.account_being_created,
                StorageErrorCode.resource_already_exists,
                StorageErrorCode.resource_type_mismatch,
                StorageErrorCode.blob_already_exists,
                StorageErrorCode.queue_already_exists,
                StorageErrorCode.container_already_exists,
                StorageErrorCode.container_being_deleted,
                StorageErrorCode.queue_being_deleted,
                StorageErrorCode.share_already_exists,
                StorageErrorCode.share_being_deleted,
            ]:
                raise_error = ResourceExistsError
    except ValueError:
        # Got an unknown error code
        pass

    # Error message should include all the error properties
    try:
        error_message += f"\nErrorCode:{error_code.value}"
    except AttributeError:
        error_message += f"\nErrorCode:{error_code}"
    for name, info in additional_data.items():
        error_message += f"\n{name}:{info}"

    if additional_data.get("headername") == "x-ms-version" and error_code == StorageErrorCode.INVALID_HEADER_VALUE:
        error_message = (
            "The provided service version is not enabled on this storage account."
            + f"Please see {SV_DOCS_URL} for additional information.\n"
            + error_message
        )

    # No need to create an instance if it has already been serialized by the generated layer
    if serialized:
        storage_error.message = error_message
        error = storage_error
    else:
        error = raise_error(message=error_message, response=storage_error.response)
    # Ensure these properties are stored in the error instance as well (not just the error message)
    error.error_code = error_code
    error.additional_info = additional_data
    # error.args is what's surfaced on the traceback - show error message in all cases
    error.args = (error.message,)
    try:
        # `from None` prevents us from double printing the exception (suppresses generated layer error context)
        exec("raise error from None")  # pylint: disable=exec-used # nosec
    except SyntaxError as exc:
        raise error from exc


def parse_to_internal_user_delegation_key(service_user_delegation_key):
    internal_user_delegation_key = UserDelegationKey()
    internal_user_delegation_key.signed_oid = service_user_delegation_key.signed_oid
    internal_user_delegation_key.signed_tid = service_user_delegation_key.signed_tid
    internal_user_delegation_key.signed_start = _to_utc_datetime(service_user_delegation_key.signed_start)
    internal_user_delegation_key.signed_expiry = _to_utc_datetime(service_user_delegation_key.signed_expiry)
    internal_user_delegation_key.signed_service = service_user_delegation_key.signed_service
    internal_user_delegation_key.signed_version = service_user_delegation_key.signed_version
    internal_user_delegation_key.value = service_user_delegation_key.value
    return internal_user_delegation_key
