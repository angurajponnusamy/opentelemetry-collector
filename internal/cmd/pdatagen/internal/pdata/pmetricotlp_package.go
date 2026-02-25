// Copyright The OpenTelemetry Authors
// SPDX-License-Identifier: Apache-2.0

package pdata // import "go.opentelemetry.io/collector/internal/cmd/pdatagen/internal/pdata"

import (
	"path/filepath"

	"go.opentelemetry.io/collector/internal/cmd/pdatagen/internal/proto"
)

var pmetricotlp = &Package{
	info: &PackageInfo{
		name: "pmetricotlp",
		path: filepath.Join("pmetric", "pmetricotlp"),
		imports: []string{
			`"encoding/binary"`,
			`"fmt"`,
			`"iter"`,
			`"math"`,
			`"sort"`,
			`"sync"`,
			``,
			`"go.opentelemetry.io/collector/pdata/internal"`,
			`"go.opentelemetry.io/collector/pdata/internal/json"`,
			`"go.opentelemetry.io/collector/pdata/internal/proto"`,
		},
		testImports: []string{
			`"strconv"`,
			`"testing"`,
			``,
			`"github.com/stretchr/testify/assert"`,
			`"github.com/stretchr/testify/require"`,
			`"google.golang.org/protobuf/proto"`,
			`gootlpcollectormetrics "go.opentelemetry.io/proto/slim/otlp/collector/metrics/v1"`,
			`govirtanacollectormetrics "go.virtana.io/vdc/proto/collector/metrics/v1"`,
			``,
			`"go.opentelemetry.io/collector/pdata/internal"`,
		},
	},
	structs: []baseStruct{
		exportMetricsResponse,
		exportMetricsPartialSuccess,
	},
}

var exportMetricsResponse = &messageStruct{
	structName:    "ExportResponse",
	description:   "// ExportResponse represents the response for gRPC/HTTP client/server.",
	protoName:     "ExportMetricsServiceResponse",
	upstreamProto: "govirtanacollectormetrics.ExportMetricsServiceResponse",
	fields: []Field{
		&MessageField{
			fieldName:     "PartialSuccess",
			protoID:       1,
			returnMessage: exportMetricsPartialSuccess,
		},
	},
}

var exportMetricsPartialSuccess = &messageStruct{
	structName:    "ExportPartialSuccess",
	description:   "// ExportPartialSuccess represents the details of a partially successful export request.",
	protoName:     "ExportMetricsPartialSuccess",
	upstreamProto: "govirtanacollectormetrics.ExportMetricsPartialSuccess",
	fields: []Field{
		&PrimitiveField{
			fieldName: "RejectedDataPoints",
			protoID:   1,
			protoType: proto.TypeInt64,
		},
		&PrimitiveField{
			fieldName: "ErrorMessage",
			protoID:   2,
			protoType: proto.TypeString,
		},
	},
}
