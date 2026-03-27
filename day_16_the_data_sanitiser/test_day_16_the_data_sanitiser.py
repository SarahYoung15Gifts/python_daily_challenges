from importlib import util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("day_16_the_data_sanitiser.py")
SPEC = util.spec_from_file_location("day16_module", MODULE_PATH)
DAY16 = util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(DAY16)


def test_get_median_returns_middle_value_for_odd_length_lists():
	assert DAY16.get_median([10, 2, 38, 23, 38, 23, 21]) == 23


def test_get_median_returns_average_for_even_length_lists():
	assert DAY16.get_median([10, 2, 38, 23, 38, 23]) == 23.0


def test_get_median_does_not_mutate_input():
	values = [3, 1, 2]

	DAY16.get_median(values)

	assert values == [3, 1, 2]


def test_get_median_raises_for_empty_lists():
	with pytest.raises(ValueError, match="data_list cannot be empty"):
		DAY16.get_median([])


def test_build_median_messages_formats_both_outputs():
	messages = DAY16.build_median_messages([3, 1, 2], [4, 1, 3, 2])

	assert messages == ["Median for list a: 2", "Median for list b: 2.5"]