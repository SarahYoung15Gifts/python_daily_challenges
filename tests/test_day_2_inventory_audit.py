from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "day_2_inventory_audit" / "day_2_inventory_audit.py"


def load_module():
	module_name = "day2_inventory_audit_module"
	spec = util.spec_from_file_location(module_name, MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_inventory_audit_prints_expected_alerts(capsys):
	module = load_module()

	assert module.inventory["Bananas"] == 5
	assert module.inventory["Cherries"] == 0
	output = capsys.readouterr().out.splitlines()
	assert output == [
		"Bananas is low in stock (5 left)",
		"Cherries is out of stock",
		"Eggplant is low in stock (8 left)",
	]
