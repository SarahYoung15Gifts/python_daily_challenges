from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("trip_calculator.py")


def load_module(monkeypatch, inputs):
	responses = iter(inputs)
	monkeypatch.setattr("builtins.input", lambda _prompt="": next(responses))
	spec = util.spec_from_file_location("trip_calculator_module", MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_calculate_trip_cost_returns_expected_total(monkeypatch, capsys):
	module = load_module(monkeypatch, ["300", "25", "3.5"])

	assert module.calculate_trip_cost(300, 25, 3.5) == 42.0
	assert capsys.readouterr().out.strip() == "Trip cost: $42.00"
