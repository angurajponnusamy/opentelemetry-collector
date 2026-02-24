
import re

commit_hash = "5b3bd3f3c"
fork_repo = "github.com/angurajponnusamy/opentelemetry-collector"

replaces = [
    "go.opentelemetry.io/collector => ../../",
    "go.opentelemetry.io/collector/client => ../../client",
    "go.opentelemetry.io/collector/component => ../../component",
    "go.opentelemetry.io/collector/component/componenttest => ../../component/componenttest",
    "go.opentelemetry.io/collector/component/componentstatus => ../../component/componentstatus",
    "go.opentelemetry.io/collector/config/configauth => ../../config/configauth",
    "go.opentelemetry.io/collector/config/configcompression => ../../config/configcompression",
    "go.opentelemetry.io/collector/config/configgrpc => ../../config/configgrpc",
    "go.opentelemetry.io/collector/config/confighttp => ../../config/confighttp",
    "go.opentelemetry.io/collector/config/configmiddleware => ../../config/configmiddleware",
    "go.opentelemetry.io/collector/config/confignet => ../../config/confignet",
    "go.opentelemetry.io/collector/config/configopaque => ../../config/configopaque",
    "go.opentelemetry.io/collector/config/configoptional => ../../config/configoptional",
    "go.opentelemetry.io/collector/config/configretry => ../../config/configretry",
    "go.opentelemetry.io/collector/config/configtelemetry => ../../config/configtelemetry",
    "go.opentelemetry.io/collector/config/configtls => ../../config/configtls",
    "go.opentelemetry.io/collector/confmap => ../../confmap",
    "go.opentelemetry.io/collector/confmap/xconfmap => ../../confmap/xconfmap",
    "go.opentelemetry.io/collector/confmap/provider/envprovider => ../../confmap/provider/envprovider",
    "go.opentelemetry.io/collector/confmap/provider/fileprovider => ../../confmap/provider/fileprovider",
    "go.opentelemetry.io/collector/confmap/provider/httpprovider => ../../confmap/provider/httpprovider",
    "go.opentelemetry.io/collector/confmap/provider/httpsprovider => ../../confmap/provider/httpsprovider",
    "go.opentelemetry.io/collector/confmap/provider/yamlprovider => ../../confmap/provider/yamlprovider",
    "go.opentelemetry.io/collector/consumer => ../../consumer",
    "go.opentelemetry.io/collector/consumer/xconsumer => ../../consumer/xconsumer",
    "go.opentelemetry.io/collector/consumer/consumererror => ../../consumer/consumererror",
    "go.opentelemetry.io/collector/consumer/consumererror/xconsumererror => ../../consumer/consumererror/xconsumererror",
    "go.opentelemetry.io/collector/consumer/consumertest => ../../consumer/consumertest",
    "go.opentelemetry.io/collector/connector => ../../connector",
    "go.opentelemetry.io/collector/connector/connectortest => ../../connector/connectortest",
    "go.opentelemetry.io/collector/connector/xconnector => ../../connector/xconnector",
    "go.opentelemetry.io/collector/connector/forwardconnector => ../../connector/forwardconnector",
    "go.opentelemetry.io/collector/exporter => ../../exporter",
    "go.opentelemetry.io/collector/exporter/debugexporter => ../../exporter/debugexporter",
    "go.opentelemetry.io/collector/exporter/exportertest => ../../exporter/exportertest",
    "go.opentelemetry.io/collector/exporter/xexporter => ../../exporter/xexporter",
    "go.opentelemetry.io/collector/exporter/exporterhelper => ../../exporter/exporterhelper",
    "go.opentelemetry.io/collector/exporter/exporterhelper/xexporterhelper => ../../exporter/exporterhelper/xexporterhelper",
    "go.opentelemetry.io/collector/exporter/nopexporter => ../../exporter/nopexporter",
    "go.opentelemetry.io/collector/exporter/otlpexporter => ../../exporter/otlpexporter",
    "go.opentelemetry.io/collector/exporter/otlphttpexporter => ../../exporter/otlphttpexporter",
    "go.opentelemetry.io/collector/extension => ../../extension",
    "go.opentelemetry.io/collector/extension/extensionauth => ../../extension/extensionauth",
    "go.opentelemetry.io/collector/extension/extensionauth/extensionauthtest => ../../extension/extensionauth/extensionauthtest",
    "go.opentelemetry.io/collector/extension/extensioncapabilities => ../../extension/extensioncapabilities",
    "go.opentelemetry.io/collector/extension/extensionmiddleware => ../../extension/extensionmiddleware",
    "go.opentelemetry.io/collector/extension/extensionmiddleware/extensionmiddlewaretest => ../../extension/extensionmiddleware/extensionmiddlewaretest",
    "go.opentelemetry.io/collector/extension/extensiontest => ../../extension/extensiontest",
    "go.opentelemetry.io/collector/extension/memorylimiterextension => ../../extension/memorylimiterextension",
    "go.opentelemetry.io/collector/extension/xextension => ../../extension/xextension",
    "go.opentelemetry.io/collector/extension/zpagesextension => ../../extension/zpagesextension",
    "go.opentelemetry.io/collector/featuregate => ../../featuregate",
    "go.opentelemetry.io/collector/internal/componentalias => ../../internal/componentalias",
    "go.opentelemetry.io/collector/internal/memorylimiter => ../../internal/memorylimiter",
    "go.opentelemetry.io/collector/internal/fanoutconsumer => ../../internal/fanoutconsumer",
    "go.opentelemetry.io/collector/internal/telemetry => ../../internal/telemetry",
    "go.opentelemetry.io/collector/internal/sharedcomponent => ../../internal/sharedcomponent",
    "go.opentelemetry.io/collector/internal/testutil => ../../internal/testutil",
    "go.opentelemetry.io/collector/otelcol => ../../otelcol",
    "go.opentelemetry.io/collector/pdata => ../../pdata",
    "go.opentelemetry.io/collector/pdata/testdata => ../../pdata/testdata",
    "go.opentelemetry.io/collector/pdata/pprofile => ../../pdata/pprofile",
    "go.opentelemetry.io/collector/pdata/xpdata => ../../pdata/xpdata",
    "go.opentelemetry.io/collector/pipeline => ../../pipeline",
    "go.opentelemetry.io/collector/pipeline/xpipeline => ../../pipeline/xpipeline",
    "go.opentelemetry.io/collector/processor => ../../processor",
    "go.opentelemetry.io/collector/processor/processortest => ../../processor/processortest",
    "go.opentelemetry.io/collector/processor/batchprocessor => ../../processor/batchprocessor",
    "go.opentelemetry.io/collector/processor/memorylimiterprocessor => ../../processor/memorylimiterprocessor",
    "go.opentelemetry.io/collector/processor/xprocessor => ../../processor/xprocessor",
    "go.opentelemetry.io/collector/processor/processorhelper/xprocessorhelper => ../../processor/processorhelper/xprocessorhelper",
    "go.opentelemetry.io/collector/processor/processorhelper => ../../processor/processorhelper",
    "go.opentelemetry.io/collector/receiver => ../../receiver",
    "go.opentelemetry.io/collector/receiver/nopreceiver => ../../receiver/nopreceiver",
    "go.opentelemetry.io/collector/receiver/receiverhelper => ../../receiver/receiverhelper",
    "go.opentelemetry.io/collector/receiver/otlpreceiver => ../../receiver/otlpreceiver",
    "go.opentelemetry.io/collector/receiver/receivertest => ../../receiver/receivertest",
    "go.opentelemetry.io/collector/receiver/xreceiver => ../../receiver/xreceiver",
    "go.opentelemetry.io/collector/service => ../../service",
    "go.opentelemetry.io/collector/service/hostcapabilities => ../../service/hostcapabilities",
    "go.opentelemetry.io/collector/service/telemetry/telemetrytest => ../../service/telemetry/telemetrytest",
    "go.virtana.io/vdc => ../../protocols/virtana/vdc",
]

config = """dist:
  name: datasender
  description: Virtana Data Sender
  output_path: ./dist
  version: 0.1.0

exporters:
  - gomod: go.opentelemetry.io/collector/exporter/debugexporter v0.0.1
  - gomod: go.opentelemetry.io/collector/exporter/otlpexporter v0.0.1

receivers:
  - gomod: go.opentelemetry.io/collector/receiver/otlpreceiver v0.0.1

processors:
  - gomod: go.opentelemetry.io/collector/processor/batchprocessor v0.0.1

replaces:
"""

for line in replaces:
    module_path = line.split(" => ")[0]
    if "go.virtana.io/vdc" in module_path:
        config += f"  - {module_path} => {fork_repo}/protocols/virtana/vdc {commit_hash}\n"
        continue

    submodule = module_path.replace("go.opentelemetry.io/collector", "")
    if submodule.startswith("/"):
        submodule = submodule[1:]
    
    if submodule:
        remote_path = f"{fork_repo}/{submodule}"
    else:
        remote_path = fork_repo
        
    config += f"  - {module_path} => {remote_path} {commit_hash}\n"

with open("virtana-build/builder-config-remote-short.yaml", "w") as f:
    f.write(config)

print("Remote config generated successfully.")
