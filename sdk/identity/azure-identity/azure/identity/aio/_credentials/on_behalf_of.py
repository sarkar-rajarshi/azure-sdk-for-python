# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import logging
from typing import Optional, Union, Any, Dict, Callable

from azure.core.exceptions import ClientAuthenticationError
from azure.core.credentials import AccessTokenInfo
from .._internal import AadClient, AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin
from ..._credentials.certificate import get_client_credential
from ..._internal import AadClientCertificate, validate_tenant_id

_LOGGER = logging.getLogger(__name__)


class OnBehalfOfCredential(AsyncContextManager, GetTokenMixin):
    """Authenticates a service principal via the on-behalf-of flow.

    This flow is typically used by middle-tier services that authorize requests to other services with a delegated
    user identity. Because this is not an interactive authentication flow, an application using it must have admin
    consent for any delegated permissions before requesting tokens for them. See `Microsoft Entra ID documentation
    <https://learn.microsoft.com/entra/identity-platform/v2-oauth2-on-behalf-of-flow>`__ for a more detailed
    description of the on-behalf-of flow.

    :param str tenant_id: ID of the service principal's tenant. Also called its "directory" ID.
    :param str client_id: The service principal's client ID.
    :keyword str client_secret: Optional. A client secret to authenticate the service principal.
        One of **client_secret**, **client_certificate**, or **client_assertion_func** must be provided.
    :keyword bytes client_certificate: Optional. The bytes of a certificate in PEM or PKCS12 format including
        the private key to authenticate the service principal. One of **client_secret**, **client_certificate**,
        or **client_assertion_func** must be provided.
    :keyword client_assertion_func: Optional. Function that returns client assertions that authenticate the
        application to Microsoft Entra ID. This function is called each time the credential requests a token. It must
        return a valid assertion for the target resource.
    :paramtype client_assertion_func: Callable[[], str]
    :keyword str user_assertion: Required. The access token the credential will use as the user assertion when
        requesting on-behalf-of tokens.

    :keyword str authority: Authority of a Microsoft Entra endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword password: A certificate password. Used only when **client_certificate** is provided. If this value
        is a unicode string, it will be encoded as UTF-8. If the certificate requires a different encoding, pass
        appropriately encoded bytes instead.
    :paramtype password: str or bytes
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_on_behalf_of_credential_async]
            :end-before: [END create_on_behalf_of_credential_async]
            :language: python
            :dedent: 4
            :caption: Create an OnBehalfOfCredential.
    """

    def __init__(
        self,
        tenant_id: str,
        client_id: str,
        *,
        client_certificate: Optional[bytes] = None,
        client_secret: Optional[str] = None,
        client_assertion_func: Optional[Callable[[], str]] = None,
        user_assertion: str,
        password: Optional[Union[str, bytes]] = None,
        **kwargs: Any
    ) -> None:
        super().__init__()
        validate_tenant_id(tenant_id)

        self._assertion = user_assertion
        if not self._assertion:
            raise TypeError('"user_assertion" must not be empty.')

        if client_assertion_func:
            if client_certificate or client_secret:
                raise ValueError(
                    "It is invalid to specify more than one of the following: "
                    '"client_assertion_func", "client_certificate" or "client_secret".'
                )
            self._client_credential: Union[str, AadClientCertificate, Dict[str, Any]] = {
                "client_assertion": client_assertion_func,
            }
        elif client_certificate:
            if client_secret:
                raise ValueError('Specifying both "client_certificate" and "client_secret" is not valid.')
            try:
                cert = get_client_credential(None, password, client_certificate)
            except ValueError as ex:
                message = '"client_certificate" is not a valid certificate in PEM or PKCS12 format'
                raise ValueError(message) from ex
            self._client_credential = AadClientCertificate(cert["private_key"], password=cert.get("passphrase"))
        elif client_secret:
            self._client_credential = client_secret
        else:
            raise TypeError('Either "client_certificate", "client_secret", or "client_assertion_func" must be provided')

        # note AadClient handles "authority" and any pipeline kwargs
        self._client = AadClient(tenant_id, client_id, **kwargs)

    async def __aenter__(self) -> "OnBehalfOfCredential":
        await self._client.__aenter__()
        return self

    async def close(self) -> None:
        """Close the credential's underlying HTTP client."""
        await self._client.close()

    async def _acquire_token_silently(self, *scopes: str, **kwargs: Any) -> Optional[AccessTokenInfo]:
        return self._client.get_cached_access_token(scopes, **kwargs)

    async def _request_token(self, *scopes: str, **kwargs: Any) -> AccessTokenInfo:
        # Note we assume the cache has tokens for one user only. That's okay because each instance of this class is
        # locked to a single user (assertion). This assumption will become unsafe if this class allows applications
        # to change an instance's assertion.
        refresh_tokens = self._client.get_cached_refresh_tokens(scopes, **kwargs)
        if len(refresh_tokens) == 1:  # there should be only one
            try:
                refresh_token = refresh_tokens[0]["secret"]
                return await self._client.obtain_token_by_refresh_token_on_behalf_of(
                    scopes, self._client_credential, refresh_token, **kwargs
                )
            except ClientAuthenticationError as ex:
                _LOGGER.debug("silent authentication failed: %s", ex, exc_info=True)
            except (IndexError, KeyError, TypeError) as ex:
                # this is purely defensive, hasn't been observed in practice
                _LOGGER.debug("silent authentication failed due to malformed refresh token: %s", ex, exc_info=True)

        # we don't have a refresh token, or silent auth failed: acquire a new token from the assertion
        return await self._client.obtain_token_on_behalf_of(scopes, self._client_credential, self._assertion, **kwargs)
