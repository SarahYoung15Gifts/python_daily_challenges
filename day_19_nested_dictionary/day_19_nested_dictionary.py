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

def calculate_average_age(company_data):
    total_age = 0
    employee_count = 0

    for employees in company_data.values():
        for employee in employees:
            total_age += employee["age"]
            employee_count += 1

    return total_age / employee_count


def main():
    print(f"Average age of employees: {calculate_average_age(company):.2f}")


if __name__ == "__main__":
    main()

    #script to run the code: python day_19_nested_dictionary.py