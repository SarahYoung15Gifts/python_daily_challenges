raw_data = """John,Sales,50000
Jane,Engineering,70000
Joe,Sales,60000
Janet,Marketing,55000
Jack,Sales,45000"""

def calculate_department_totals(data):
	department_totals = {}
	for line in data.splitlines():
		_name, dept, salary = line.split(",")
		salary = int(salary)
		if dept in department_totals:
			department_totals[dept] += salary
		else:
			department_totals[dept] = salary
	return department_totals


def main():
	print(calculate_department_totals(raw_data))


if __name__ == "__main__":
	main()
		
# script to run in terminal with: python day_18_the_dynamic_accountant.py