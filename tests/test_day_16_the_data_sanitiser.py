from importlib import util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).resolve().parents[1] / "day_16_the_data_sanitiser" / "day_16_the_data_sanitser.py"


def load_module():
	spec = util.spec_from_file_location("day16_module", MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_get_median_returns_middle_value_for_odd_length_lists(capsys):
	module = load_module()

	assert module.get_median([10, 2, 38, 23, 38, 23, 21]) == 23
	capsys.readouterr()


def test_get_median_returns_average_for_even_length_lists(capsys):
	module = load_module()

	assert module.get_median([10, 2, 38, 23, 38, 23]) == 23.0
	capsys.readouterr()


def test_get_median_sorts_input_in_place(capsys):
	module = load_module()
	values = [3, 1, 2]

	module.get_median(values)

	assert values == [1, 2, 3]
	capsys.readouterr()


def test_get_median_raises_for_empty_lists(capsys):
	module = load_module()

	with pytest.raises(ValueError, match="data_list cannot be empty"):
		module.get_median([])
	capsys.readouterr()


def test_module_prints_expected_median_output(capsys):
	load_module()

	assert capsys.readouterr().out.splitlines() == [
		"Median for list a: 23",
		"Median for list b: 23.0",
	]