Implementation Plan - Update pdata/pmetric for vdcpmetric
Update the pdata (OpenTelemetry Data) layer to support custom vdc fields in 
ResourceMetrics and Resource, based on the custom metrics.proto, resource.proto, and meta.proto.

Prerequisites 
——————————
1. Under protocols/virtana/vdc folder make sure all your *.proto files are exists and also its  *.pb.go files

Proposed Changes
———————————
[MODIFY] go.mod
* Add replace go.virtana.io/vdc => ../protocols/virtana/vdc if not already present.
* Add go.virtana.io/vdc to required modules.

Go to internal/cmd/pdatagen/pdata

[MODIFY] pcommon_package.go
* Add metaData message struct definition.
* Update resource message struct to include EntityGuid, EntityType, and EntityName primitive fields.
* Add metaData to the pcommon.structs list.

[MODIFY] pmetric_package.go
* Update resourceMetrics message struct to include the Meta field (pointing to metaData).
* Update testImports to include Virtana proto packages for verification in tests.


Verification Steps
——————————
Automated Tests
* Run make genpdata to regenerate all pdata files.
* Run go test ./pdata/... to ensure everything compiles and basic tests pass.
* Create a new test case in pdata/pmetric/metrics_test.go (or similar) to verify that the new fields are accessible and correctly mapped to the underlying protobuf.
bash

make genpdata
go test -v ./pdata/pmetric/...
go test -v ./pdata/pcommon/...
Manual Verification
* Inspect pdata/pmetric/generated_resourcemetrics.go to ensure Meta() and SetMeta() methods are present.
* Inspect pdata/pcommon/generated_resource.go to ensure EntityGuid(), EntityType(), and EntityName() methods are present.