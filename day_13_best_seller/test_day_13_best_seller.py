from importlib import util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("day_13_best_seller.py")
SPEC = util.spec_from_file_location("day13_module", MODULE_PATH)
DAY13 = util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(DAY13)


def test_calculate_sale_total_multiplies_quantity_by_price():
	sale = {"item": "Notebook", "quantity": 4, "price": 2.5}

	assert DAY13.calculate_sale_total(sale) == 10.0


def test_get_best_selling_items_returns_all_tied_items():
	item_totals = {"Notebook": 7, "Pen": 10, "Pencil": 10}

	assert DAY13.get_best_selling_items(item_totals) == ["Pen", "Pencil"]


def test_summarize_sales_builds_expected_report():
	report = DAY13.summarize_sales(DAY13.sales)

	assert report[0] == "Notebook: 4 x $2.50 = $10.00"
	assert report[-2] == "Total Revenue: $77.50"
	assert report[-1] == "Best-Selling Items: Pen, Pencil"
