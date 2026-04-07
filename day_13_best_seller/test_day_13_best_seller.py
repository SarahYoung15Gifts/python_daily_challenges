from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("day_13_best_seller.py")


def load_module():
	spec = util.spec_from_file_location("day13_module", MODULE_PATH)
	module = util.module_from_spec(spec)
	assert spec is not None and spec.loader is not None
	spec.loader.exec_module(module)
	return module


def test_calculate_sale_total_multiplies_quantity_by_price(capsys):
	module = load_module()

	assert module.calculate_sale_total({"item": "Notebook", "quantity": 4, "price": 2.5}) == 10.0
	capsys.readouterr()


def test_get_best_selling_items_returns_all_tied_items(capsys):
	module = load_module()

	assert module.get_best_selling_items({"Notebook": 7, "Pen": 10, "Pencil": 10}) == ["Pen", "Pencil"]
	capsys.readouterr()


def test_module_calculates_sales_summary_and_output(capsys):
	module = load_module()

	assert module.total_revenue == 77.5
	assert module.best_selling_items == ["Pen", "Pencil"]
	output = capsys.readouterr().out.splitlines()
	assert output[0] == "Notebook: 4 x $2.50 = $10.00"
	assert output[-2] == "Total Revenue: $77.50"
	assert output[-1] == "Best-Selling Items: Pen, Pencil"
