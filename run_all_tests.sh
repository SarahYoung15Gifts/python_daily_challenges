#!/usr/bin/env sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

"$SCRIPT_DIR/.venv/bin/python" -m pytest -q \
	"$SCRIPT_DIR/day_6_trip_calculator/test_trip_calculator.py" \
	"$SCRIPT_DIR/day_12_modular_validator/test_day_12_modular_validator.py" \
	"$SCRIPT_DIR/day_13_best_seller/test_day_13_best_seller.py" \
	"$SCRIPT_DIR/day_15_library_system/test_day_15_library_system.py" \
	"$SCRIPT_DIR/day_16_the_data_sanitiser/test_day_16_the_data_sanitiser.py"