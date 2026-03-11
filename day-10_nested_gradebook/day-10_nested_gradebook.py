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

# "star_student" is a variable that will hold the name of the student with the highest average grade.
star_student = ""
# "highest_average" is a variable that will hold the highest average grade found so far. It is initialized to 0.
highest_average = 0

# A for loop is used to iterate through each student in the students list. 
# The variable "student" represents the current student being processed in each iteration of the loop.
for student in students:
    # "name" is assigned the value of the "name" key from the current student dictionary.
    # "grades" is assigned the value of the "grades" key from the current student dictionary.
    name = student["name"]
    # "grades" is assigned the value of the "grades" key from the current student dictionary.
    grades = student["grades"]
    # This is the calculation of the average grade for the current student. It sums up all the grades and divides by the number of grades to get the average.
    # "len" is a built-in function that returns the number of items in a list, which in this case is the number of grades.
    # It then rounds the average to 2 decimal places using the "round" function.
    average = round(sum(grades) / len(grades), 2)

    print(f"{name}: Average = {average}")

# This if statement checks if the average grade of the current student is greater than the highest average found so far.
# If it is, it updates the highest_average variable to the current average and sets the star_student variable to the current student's name.
    if average > highest_average:
        highest_average = average
        star_student = name

print(f"Star Student: {star_student}")

# script to run: python day-10_nested_gradebook.py
