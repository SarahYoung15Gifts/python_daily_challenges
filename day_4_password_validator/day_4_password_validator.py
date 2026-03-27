def validate_password(password):
	reasons = []
	if len(password) < 8:
		reasons.append("- Must be at least 8 characters long.")
	if not any(character.isdigit() for character in password):
		reasons.append("- Must contain at least one number.")
	if "!" not in password:
		reasons.append("- Must contain at least one exclamation mark (!).")
	return len(reasons) == 0, reasons


def main():
	password = input("Enter a password: ")
	is_valid, reasons = validate_password(password)
	if is_valid:
		print("Password secure!")
	else:
		print("Password too weak!")
		for reason in reasons:
			print(reason)


if __name__ == "__main__":
	main()

# script to run: python day_4_password_validator.py