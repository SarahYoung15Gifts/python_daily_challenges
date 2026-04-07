#!/usr/bin/env sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

"$SCRIPT_DIR/.venv/bin/python" -m pytest -q "$SCRIPT_DIR/day_15_library_system/test_day_15_library_system.py"