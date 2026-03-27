raw_data = """John,Sales,50000
Jane,Engineering,70000
Joe,Sales,60000
Janet,Marketing,55000
Jack,Sales,45000"""

def parse_rows(data):
	return [line.split(",") for line in data.splitlines()]


def calculate_payroll_totals(rows):
	totals = {
		"Sales": 0,
		"Engineering": 0,
		"Marketing": 0,
	}
	for row in rows:
		department = row[1]
		totals[department] += int(row[2])
	totals["Total"] = sum(totals.values())
	return totals


def build_payroll_report(totals):
	return [
		f"Total Sales Payroll: {totals['Sales']}",
		f"Total Engineering Payroll: {totals['Engineering']}",
		f"Total Marketing Payroll: {totals['Marketing']}",
		f"Total Payroll: {totals['Total']}",
	]


def main():
	totals = calculate_payroll_totals(parse_rows(raw_data))
	for line in build_payroll_report(totals):
		print(line)


if __name__ == "__main__":
	main()

# Run in terminal with: python day_17_csv_parser.py