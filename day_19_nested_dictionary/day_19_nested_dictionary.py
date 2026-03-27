# Nested Dictionary Example.
# "company" is a dictionary where each key is a department and the value is a list of dictionaries representing employees in that department.
company = {
    "Sales": [
        {"name": "Alice", "age": 28},
        {"name": "Bob", "age": 34}
    ],
    "Engineering": [
        {"name": "Charlie", "age": 22},
        {"name": "David", "age": 45},
        {"name": "Eve", "age": 30}
    ]
}

total_age = 0
employee_count = 0

for department in company:
    for employee in company[department]:
        total_age += employee["age"]
        employee_count += 1

print(f"Average age of employees: {total_age / employee_count:.2f}")

    #script to run the code: python day_19_nested_dictionary.py