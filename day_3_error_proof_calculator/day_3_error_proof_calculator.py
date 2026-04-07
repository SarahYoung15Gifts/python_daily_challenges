# This snippet is a definition of a function that takes a number as an input and returns half of that number.
def calculate_half(number):
    return number / 2

def format_half_result(number):
    return f"Half of {number} is {calculate_half(number)}."


def run_calculator(reader=None, writer=None):
    reader = reader or input
    writer = writer or print

    try:
        user_number = float(reader("Type a number: "))
        writer(format_half_result(user_number))
    except ValueError:
        writer("That's not a number!")


def main():
    run_calculator()


if __name__ == "__main__":
    main()

#script to run: python error-proof-calculator.py