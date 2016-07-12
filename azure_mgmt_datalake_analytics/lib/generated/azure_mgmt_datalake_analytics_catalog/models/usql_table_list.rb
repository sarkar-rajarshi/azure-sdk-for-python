# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::DataLakeAnalytics::Catalog
  module Models
    #
    # A Data Lake Analytics catalog U-SQL table item list.
    #
    class USqlTableList < CatalogItemList

      include MsRestAzure

      # @return [Array<USqlTable>] the list of tables in the database and
      # schema combination
      attr_accessor :value


      #
      # Mapper for USqlTableList class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'USqlTableList',
          type: {
            name: 'Composite',
            class_name: 'USqlTableList',
            model_properties: {
              count: {
                required: false,
                serialized_name: 'count',
                type: {
                  name: 'Number'
                }
              },
              next_link: {
                required: false,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              },
              value: {
                required: false,
                read_only: true,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'USqlTableElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'USqlTable'
                      }
                  }
                }
              }
            }
          }
        }
      end
    end
  end
end
