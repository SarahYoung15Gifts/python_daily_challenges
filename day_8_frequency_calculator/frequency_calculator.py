# This is a list called 'votes' that contains the votes for different fruits. 
# Each item in the list represents a vote for a particular fruit. 
votes = ["apple", "banana", "apple", "cherry", "apple", "banana", "cherry", "cherry", "apple", "apple", "pineapple"]

def count_votes(items):
	vote_count = {}
	for fruit in items:
		if fruit in vote_count:
			vote_count[fruit] += 1
		else:
			vote_count[fruit] = 1
	return vote_count


def main():
	print(count_votes(votes))


if __name__ == "__main__":
	main()

#script to run the code: python frequency_calculator.py