from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("day_19_nested_dictionary.py")


def load_module():
	module_name = "day19_nested_dictionary_module"
	spec = util.spec_from_file_location(module_name, MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_nested_dictionary_computes_average_age(capsys):
	module = load_module()

	assert module.total_age == 159
	assert module.employee_count == 5
	assert capsys.readouterr().out.strip() == "Average age of employees: 31.80"