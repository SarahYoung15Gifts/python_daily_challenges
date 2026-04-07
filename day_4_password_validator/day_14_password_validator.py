def validate_password(password):
	reasons = []
	if len(password) < 8:
		reasons.append("- Must be at least 8 characters long.")
	if not any(character.isdigit() for character in password):
		reasons.append("- Must contain at least one number.")
	if "!" not in password:
		reasons.append("- Must contain at least one exclamation mark (!).")
	return len(reasons) == 0, reasons


def get_password_feedback(password):
	is_valid, reasons = validate_password(password)
	if is_valid:
		return ["Password secure!"]
	return ["Password too weak!", *reasons]


def main(reader=None, writer=None):
	reader = reader or input
	writer = writer or print
	password = reader("Enter a password: ")
	for line in get_password_feedback(password):
		writer(line)


if __name__ == "__main__":
	main()

# script to run: python password-validator.py