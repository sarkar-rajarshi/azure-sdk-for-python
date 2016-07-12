# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::DataLakeAnalytics::Account
  module Models
    #
    # A Data Lake Analytics account object, containing all information
    # associated with the named Data Lake Analytics account.
    #
    class DataLakeAnalyticsAccount

      include MsRestAzure

      # @return [String] the account regional location.
      attr_accessor :location

      # @return [String] the account name.
      attr_accessor :name

      # @return [String] the namespace and type of the account.
      attr_accessor :type

      # @return [String] the account subscription ID.
      attr_accessor :id

      # @return [Hash{String => String}] the value of custom properties.
      attr_accessor :tags

      # @return [DataLakeAnalyticsAccountProperties] the properties defined by
      # Data Lake Analytics all properties are specific to each resource
      # provider.
      attr_accessor :properties


      #
      # Mapper for DataLakeAnalyticsAccount class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'DataLakeAnalyticsAccount',
          type: {
            name: 'Composite',
            class_name: 'DataLakeAnalyticsAccount',
            model_properties: {
              location: {
                required: false,
                serialized_name: 'location',
                type: {
                  name: 'String'
                }
              },
              name: {
                required: false,
                serialized_name: 'name',
                type: {
                  name: 'String'
                }
              },
              type: {
                required: false,
                read_only: true,
                serialized_name: 'type',
                type: {
                  name: 'String'
                }
              },
              id: {
                required: false,
                read_only: true,
                serialized_name: 'id',
                type: {
                  name: 'String'
                }
              },
              tags: {
                required: false,
                serialized_name: 'tags',
                type: {
                  name: 'Dictionary',
                  value: {
                      required: false,
                      serialized_name: 'StringElementType',
                      type: {
                        name: 'String'
                      }
                  }
                }
              },
              properties: {
                required: false,
                serialized_name: 'properties',
                type: {
                  name: 'Composite',
                  class_name: 'DataLakeAnalyticsAccountProperties'
                }
              }
            }
          }
        }
      end
    end
  end
end
