# List with all of the temperatures for the week.
# '68, 82, 71...' are integerstemps = [68, 82, 71, 89, 74, 81, 65]
temps = [68, 82, 71, 89, 74, 81, 65]

# "hot_days" is a new list that contains only the temperatures that are greater than 75.
# 'temp' is a variable that represents each temperature in the "temps" list as we loop through it.
# 'temp for temp' is a list comprehension that creates a new list by iterating over each temperature in the "temps" list and including it in the new list if it meets the condition 'temp > 75'.
hot_days = [temp for temp in temps if temp > 75]

print(f"Temperatures over 75: {hot_days}")

# 'len' is a built-in function in Python that returns the number of items in a list. 
print(f"Hot days: {len(hot_days)}")

# script to run the code: python list_filtering.py