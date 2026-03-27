from importlib import util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("day_12_modular_validator.py")
SPEC = util.spec_from_file_location("day12_module", MODULE_PATH)
DAY12 = util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(DAY12)


@pytest.mark.parametrize(
	"password",
	["LearningPython123!", "CheckMe@123"],
)
def test_is_strong_accepts_valid_passwords(password):
	assert DAY12.is_strong(password) is True


@pytest.mark.parametrize(
	"password",
	["short!A", "nouppercase123!", "MissingSpecial123"],
)
def test_is_strong_rejects_invalid_passwords(password):
	assert DAY12.is_strong(password) is False


def test_describe_password_returns_valid_message():
	message = DAY12.describe_password("LearningPython123!")

	assert message == "LearningPython123! is a valid password."


def test_describe_password_returns_invalid_message():
	message = DAY12.describe_password("pythonisgreat!")

	assert message == "pythonisgreat! is an invalid password."
