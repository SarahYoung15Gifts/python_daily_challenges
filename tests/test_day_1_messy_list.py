from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "day_1_messy_list" / "day_1_messy_list.py"


def load_module():
	module_name = "day1_messy_list_module"
	spec = util.spec_from_file_location(module_name, MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_clean_list_contains_normalized_names(capsys):
	module = load_module()

	assert module.clean_list == ["Alice", "Bob", "Charlie", "Daisy", "Eve"]
	output = capsys.readouterr().out.splitlines()
	assert output == [
		"You are invited, Alice!",
		"You are invited, Bob!",
		"You are invited, Charlie!",
		"You are invited, Daisy!",
		"You are invited, Eve!",
	]
