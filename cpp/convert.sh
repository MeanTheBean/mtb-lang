#!/bin/bash

# Script dir & input dir
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_DIR="$(dirname "$SCRIPT_DIR")"
OUT_DIR="$SCRIPT_DIR"

echo "Embedding all .py files from $SRC_DIR into $OUT_DIR ... >w<"

for f in "$SRC_DIR"/*.py; do
    if [[ -f "$f" ]]; then
        filename=$(basename -- "$f")
        name_no_ext="${filename%.py}"

        # Generate header with xxd
        # Then fix variable names, keep types intact
        xxd -i "$f" | \
        sed -E "s/unsigned char [^ ]+_py/unsigned char ${name_no_ext}_py/" | \
        sed -E "s/unsigned int [^ ]+_py_len/unsigned int ${name_no_ext}_py_len/" \
        > "$OUT_DIR/${name_no_ext}.h"

        echo "   🐍 Embedded $filename → ${name_no_ext}.h"
    fi
done

echo "All done nya~ 💖"
