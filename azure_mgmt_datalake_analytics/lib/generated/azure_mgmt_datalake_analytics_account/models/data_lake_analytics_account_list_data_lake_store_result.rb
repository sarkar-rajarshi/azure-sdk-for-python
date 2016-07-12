# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::DataLakeAnalytics::Account
  module Models
    #
    # Data Lake Account list information.
    #
    class DataLakeAnalyticsAccountListDataLakeStoreResult

      include MsRestAzure

      # @return [Array<DataLakeStoreAccountInfo>] the results of the list
      # operation
      attr_accessor :value

      # @return [Integer] total number of results.
      attr_accessor :count

      # @return [String] the link (url) to the next page of results.
      attr_accessor :next_link


      #
      # Mapper for DataLakeAnalyticsAccountListDataLakeStoreResult class as
      # Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'DataLakeAnalyticsAccountListDataLakeStoreResult',
          type: {
            name: 'Composite',
            class_name: 'DataLakeAnalyticsAccountListDataLakeStoreResult',
            model_properties: {
              value: {
                required: false,
                read_only: true,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'DataLakeStoreAccountInfoElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'DataLakeStoreAccountInfo'
                      }
                  }
                }
              },
              count: {
                required: false,
                read_only: true,
                serialized_name: 'count',
                type: {
                  name: 'Number'
                }
              },
              next_link: {
                required: false,
                read_only: true,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end
