from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("trip_calculator.py")
SPEC = util.spec_from_file_location("trip_calculator_module", MODULE_PATH)
TRIP_CALCULATOR = util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(TRIP_CALCULATOR)


def test_calculate_trip_cost_returns_expected_total():
	result = TRIP_CALCULATOR.calculate_trip_cost(300, 25, 3.5)

	assert result == 42.0


def test_format_trip_cost_formats_currency_to_two_decimals():
	assert TRIP_CALCULATOR.format_trip_cost(42) == "Trip cost: $42.00"
