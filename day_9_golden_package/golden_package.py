# This is a list called packages that contains elements or list items that represent different types of packages. 
packages = ["Standard", "Standard", "Fragile", "Standard", "Golden", "Standard"]

for package in packages:
	if package == "Golden":
		print("Found the Golden Package!")
		break
	elif package == "Fragile":
		print("Skipping fragile package...")
		continue
	else:
		print("Checking standard package...")

# script to run: python golden_package.py