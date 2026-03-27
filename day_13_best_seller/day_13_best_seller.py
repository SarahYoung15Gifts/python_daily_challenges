sales = [
	{"item": "Notebook", "quantity": 4, "price": 2.50},
	{"item": "Pen", "quantity": 10, "price": 1.20},
	{"item": "Pencil", "quantity": 10, "price": 1.20},
	{"item": "Backpack", "quantity": 2, "price": 18.00},
	{"item": "Notebook", "quantity": 3, "price": 2.50}
]

def calculate_sale_total(sale):
	return sale["quantity"] * sale["price"]


def get_best_selling_items(item_totals):
	highest_quantity = max(item_totals.values())
	return [item for item, qty in item_totals.items() if qty == highest_quantity]


def summarize_sales(sales_records):
	lines = []
	total_revenue = 0
	item_totals = {}

	for sale in sales_records:
		line_total = calculate_sale_total(sale)
		lines.append(
			f"{sale['item']}: {sale['quantity']} x ${sale['price']:.2f} = ${line_total:.2f}"
		)
		total_revenue += line_total
		item_totals[sale["item"]] = item_totals.get(sale["item"], 0) + sale["quantity"]

	lines.append(f"Total Revenue: ${total_revenue:.2f}")
	best_selling_items = get_best_selling_items(item_totals)
	if len(best_selling_items) == 1:
		lines.append(f"Best-Selling Item: {best_selling_items[0]}")
	else:
		lines.append(f"Best-Selling Items: {', '.join(best_selling_items)}")
	return lines


def main():
	for line in summarize_sales(sales):
		print(line)


if __name__ == "__main__":
	main()

