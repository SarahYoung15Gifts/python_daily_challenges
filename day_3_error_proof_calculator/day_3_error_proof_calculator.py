# This snippet is a definition of a function that takes a number as an input and returns half of that number.
def calculate_half(number):
    return number / 2

# A try block is used to catch any exceptions that may occur during the execution of the code.
try:
    # This part of the code prompts the user to input a number, converts it to a float, and then calls the calculate_half function with that number, printing the result.
# A float is used to allow for decimal numbers, making the calculator more versatile. If the input is not a valid number, a ValueError is handled.
    user_number = float(input("Type a number: "))
    # The result of the calculation is stored in a variable called 'result', which is then printed to the user.
    # This calls the calculate_half function with the user input.
    result = calculate_half(user_number)

    print(f"Half of {user_number} is {result}.")

    # An except block is used to catch a ValueError, which occurs if the user inputs something that cannot be converted to a float (like a string that doesn't represent a number). 
except ValueError:
    print("That's not a number!")

#script to run: python error-proof-calculator.py