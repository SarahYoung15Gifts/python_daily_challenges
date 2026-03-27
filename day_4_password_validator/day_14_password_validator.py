#prompt for the user to enter a password. This is stored in a variable called 'password'.
password = input("Enter a password: ")

# Variables to check the password criteria
# 'len' checks the length of the password.
is_long_enough = len(password) >= 8
# 'any' checks if any character in the password is a digit.
has_number = any(character.isdigit() for character in password)
# Checks if the password contains an exclamation mark.
has_exclamation = "!" in password

# If else statement to check if all criteria are met and print the appropriate message.
if is_long_enough and has_number and has_exclamation:
	print("Password secure!")
else:
	print("Password too weak!")

	if not is_long_enough:
		print("- Must be at least 8 characters long.")
	if not has_number:
		print("- Must contain at least one number.")
	if not has_exclamation:
		print("- Must contain at least one exclamation mark (!).")

# script to run: python password-validator.py