# A python 'list' that contains names with inconsistent formatting.
messy_list = [
	"  alice",
	"  BOB  ",
	"    chArLie ",
	" daisy ",
	"   EVE",
]

def clean_names(names):
	return [name.strip().capitalize() for name in names]


def build_invitation_messages(names):
	return [f"You are invited, {name}!" for name in names]


def main():
	for message in build_invitation_messages(clean_names(messy_list)):
		print(message)


if __name__ == "__main__":
	main()

#script to run: python messy-list.py