from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("day_17_csv_parser.py")


def load_module():
	module_name = "day17_csv_parser_module"
	spec = util.spec_from_file_location(module_name, MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_csv_parser_calculates_department_totals(capsys):
	module = load_module()

	assert module.rows[0] == ["John", "Sales", "50000"]
	assert module.total_sales_payroll == 155000
	assert module.total_engineering_payroll == 70000
	assert module.total_marketing_payroll == 55000
	assert module.total_payroll == 280000
	output = capsys.readouterr().out.splitlines()
	assert output == [
		"Total Sales Payroll: 155000",
		"Total Engineering Payroll: 70000",
		"Total Marketing Payroll: 55000",
		"Total Payroll: 280000",
	]
