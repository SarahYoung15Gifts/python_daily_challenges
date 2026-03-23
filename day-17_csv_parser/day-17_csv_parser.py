raw_data = """John,Sales,50000
Jane,Engineering,70000
Joe,Sales,60000
Janet,Marketing,55000
Jack,Sales,45000"""

lines = raw_data.splitlines()

rows = []
total_sales_payroll = 0
total_engineering_payroll = 0
total_marketing_payroll = 0

for line in lines:
	row = line.split(",")
	rows.append(row)

	if row[1] == "Sales":
		total_sales_payroll += int(row[2])
	if row[1] == "Engineering":
		total_engineering_payroll += int(row[2])
	if row[1] == "Marketing":
		total_marketing_payroll += int(row[2])

total_payroll = (
	total_sales_payroll
	+ total_engineering_payroll
	+ total_marketing_payroll
)

print (f"Total Sales Payroll: {total_sales_payroll}")
print (f"Total Engineering Payroll: {total_engineering_payroll}")
print (f"Total Marketing Payroll: {total_marketing_payroll}")
print (f"Total Payroll: {total_payroll}")

# Run in terminal with: python day-17_csv_parser.py