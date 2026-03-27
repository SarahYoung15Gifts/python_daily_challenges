raw_data = """John,Sales,50000
Jane,Engineering,70000
Joe,Sales,60000
Janet,Marketing,55000
Jack,Sales,45000"""

department_totals = {}

for line in raw_data.splitlines():
	name, dept, salary = line.split(",")
	salary = int(salary)

	if dept in department_totals:
		department_totals[dept] += salary
	else:
		department_totals[dept] = salary

print(department_totals)
		
# script to run in terminal with: python day_18_the_dynamic_accountant.py