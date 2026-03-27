# This is a list called packages that contains elements or list items that represent different types of packages. 
packages = ["Standard", "Standard", "Fragile", "Standard", "Golden", "Standard"]

def inspect_packages(items):
	messages = []
	for package in items:
		if package == "Golden":
			messages.append("Found the Golden Package!")
			break
		if package == "Fragile":
			messages.append("Skipping fragile package...")
			continue
		messages.append("Checking standard package...")
	return messages


def main():
	for message in inspect_packages(packages):
		print(message)


if __name__ == "__main__":
	main()

# script to run: python golden_package.py