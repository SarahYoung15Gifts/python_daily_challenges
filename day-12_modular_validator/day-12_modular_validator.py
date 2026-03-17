def is_strong(password):
    if len(password) < 10:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*" for char in password):
        return False
    return True


test_passwords = ["12345", "pythonisgreat!", "LearningPython123!", "CheckMe@123"]

for pwd in test_passwords:
    if is_strong(pwd):
        print(f"{pwd} is a valid password.")
    else:
        print(f"{pwd} is an invalid password.")


# script to run the modular validator: python day-12_modular_validator.py