curl -v -X POST http://10.10.101.190:31642/v1/metrics \
-H "Content-Type: application/json" \
-d @- <<EOF
{
  "resourceMetrics": [
    {
      "resource": {
        "entityGuid": "test-entity-guid",
        "entityType": "test-entity-type",
        "entityName": "test-entity-name",
        "attributes": [
          {
            "key": "service.name",
            "value": { "stringValue": "test-service" }
          }
        ]
      },
      "meta": {
        "configId": "test-config-id",
        "vdcId": "test-vdc-id",
        "collectionType": "test-collection-type",
        "collectionId": "test-collection-id"
      },
      "scopeMetrics": [
        {
          "scope": { "name": "test-scope" },
          "metrics": [
            {
              "name": "custom_metric",
              "description": "A custom metric for testing",
              "unit": "1",
              "sum": {
                "dataPoints": [
                  {
                    "asInt": "42",
                    "startTimeUnixNano": "$(date +%s)000000000",
                    "timeUnixNano": "$(date +%s)000000000"
                  }
                ],
                "aggregationTemporality": 1,
                "isMonotonic": true
              }
            }
          ]
        }
      ]
    }
  ]
}
EOF
