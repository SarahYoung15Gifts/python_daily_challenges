from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("frequency_calculator.py")


def load_module():
	module_name = "frequency_calculator_module"
	spec = util.spec_from_file_location(module_name, MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_vote_count_matches_expected_totals(capsys):
	module = load_module()

	assert module.vote_count == {
		"apple": 5,
		"banana": 2,
		"cherry": 3,
		"pineapple": 1,
	}
	assert capsys.readouterr().out.strip() == str(module.vote_count)
