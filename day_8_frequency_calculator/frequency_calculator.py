# This is a list called 'votes' that contains the votes for different fruits. 
# Each item in the list represents a vote for a particular fruit. 
votes = ["apple", "banana", "apple", "cherry", "apple", "banana", "cherry", "cherry", "apple", "apple", "pineapple"]

# This is an empty dictionary called 'vote_count' that will be used to store the count of votes for each fruit.
vote_count = {}

# This loop iterates through each fruit in the 'votes' list.
for fruit in votes:
	# The 'if' statement checks if the current fruit is already a key in the 'vote_count' dictionary.
	if fruit in vote_count:
		# If the fruit is already a key in the dictionary, it increments the count of votes for that fruit by 1.
		# the "+= 1" is a shorthand for "vote_count[fruit] = vote_count[fruit] + 1". It takes the current count of votes for that fruit and adds 1 to it.
		vote_count[fruit] += 1
	else:
		# If the fruit is not already a key in the dictionary, it adds the fruit as a key with a value of 1.
		vote_count[fruit] = 1

print(vote_count)

#script to run the code: python frequency_calculator.py