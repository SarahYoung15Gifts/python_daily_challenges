# A python 'list' that contains names with inconsistent formatting.
messy_list = [
	"  alice",
	"  BOB  ",
	"    chArLie ",
	" daisy ",
	"   EVE",
]

# A new variable 'clean_list' is created using 'list comprehension'. 'name' is a temporary variable that takes each value from 'messy_list' one by one. 
# The 'strip()' method removes any leading and trailing whitespace from the name, and the 'capitalize()' method converts the first character to uppercase and the rest to lowercase. 
# The resulting cleaned names are stored in 'clean_list'.
clean_list = [name.strip().capitalize() for name in messy_list]

# The code then iterates over each name in 'clean_list' and prints a personalized invitation message for each name.
for name in clean_list:
	print(f"You are invited, {name}!")

#script to run: python messy-list.py