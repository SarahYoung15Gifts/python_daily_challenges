from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "day_6_trip_calculator" / "trip_calculator.py"


def load_module():
	spec = util.spec_from_file_location("trip_calculator_module", MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_calculate_trip_cost_returns_expected_total():
	module = load_module()

	assert module.calculate_trip_cost(300, 25, 3.5) == 42.0
	assert module.format_trip_cost(42.0) == "Trip cost: $42.00"
