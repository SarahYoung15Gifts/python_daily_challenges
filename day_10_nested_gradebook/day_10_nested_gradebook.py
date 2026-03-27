# This is a list of dictionaries called students.
#"students" is a variable.
# Each dictionary represents a student and contains their name and a list of their grades.
#This is called a nested data structure because a list contains dictionaries, and each dictionary contains another list.
students = [
    # Each dictionary has two key-value pairs: "name" which is a string, and "grades" which is a list of integers.
    {"name": "Alice", "grades": [85, 90, 92]},
    {"name": "Bob", "grades": [70, 68, 72]},
    {"name": "Charlie", "grades": [100, 95, 98]},
    {"name": "David", "grades": [101, 96, 99]}
]

def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)


def build_grade_report(student_records):
    lines = []
    star_student = ""
    highest_average = 0

    for student in student_records:
        name = student["name"]
        average = calculate_average(student["grades"])
        lines.append(f"{name}: Average = {average}")
        if average > highest_average:
            highest_average = average
            star_student = name

    lines.append(f"Star Student: {star_student}")
    return lines


def main():
    for line in build_grade_report(students):
        print(line)


if __name__ == "__main__":
    main()

# script to run: python day_10_nested_gradebook.py
