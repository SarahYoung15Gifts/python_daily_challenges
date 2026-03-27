# This snippet is a definition of a function that takes a number as an input and returns half of that number.
def calculate_half(number):
    return number / 2


def format_half_result(number):
    return f"Half of {number} is {calculate_half(number)}."


def main():
    try:
        user_number = float(input("Type a number: "))
        print(format_half_result(user_number))
    except ValueError:
        print("That's not a number!")


if __name__ == "__main__":
    main()

#script to run: python error-proof-calculator.py