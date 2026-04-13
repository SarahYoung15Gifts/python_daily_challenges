from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "day_10_nested_gradebook" / "day_10_nested_gradebook.py"


def load_module():
	module_name = "day10_nested_gradebook_module"
	spec = util.spec_from_file_location(module_name, MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_gradebook_calculates_star_student_and_output(capsys):
	module = load_module()

	assert module.star_student == "David"
	assert module.highest_average == 98.67
	output = capsys.readouterr().out.splitlines()
	assert output[-1] == "Star Student: David"
	assert "Alice: Average = 89.0" in output
	assert "David: Average = 98.67" in output
