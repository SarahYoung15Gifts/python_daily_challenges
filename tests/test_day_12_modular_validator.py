from importlib import util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).resolve().parents[1] / "day_12_modular_validator" / "day_12_modular_validator.py"


def load_module():
	spec = util.spec_from_file_location("day12_module", MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


@pytest.mark.parametrize(
	"password",
	["LearningPython123!", "CheckMe@123"],
)
def test_is_strong_accepts_valid_passwords(password, capsys):
	module = load_module()

	assert module.is_strong(password) is True
	capsys.readouterr()


@pytest.mark.parametrize(
	"password",
	["short!A", "nouppercase123!", "MissingSpecial123"],
)
def test_is_strong_rejects_invalid_passwords(password, capsys):
	module = load_module()

	assert module.is_strong(password) is False
	capsys.readouterr()


def test_module_prints_expected_password_report(capsys):
	load_module()

	assert capsys.readouterr().out.splitlines() == [
		"12345 is an invalid password.",
		"pythonisgreat! is an invalid password.",
		"LearningPython123! is a valid password.",
		"CheckMe@123 is a valid password.",
	]
