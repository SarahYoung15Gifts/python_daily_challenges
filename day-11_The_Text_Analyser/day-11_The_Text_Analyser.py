# "text" is a string variable that contains a sample text for analysis.
text = "Python is amazing and Python is fun to learn. Learning Python opens many doors for a programmer."

# "text.lower" converts the entire text to lowercase, and "replace" removes the period characters from the text. 
text = text.lower().replace(".", "")

# "words" is a list that contains all the individual words from the text, obtained by splitting the text using the "split" method.
words = text.split()

# "unique_words" is a set that contains only the unique words from the "words" list, eliminating any duplicates.
# "set" is a built-in data structure in Python that automatically removes duplicate elements, so when we convert the list of words to a set, we get only the unique words.
unique_words = set(words)

# "long_words" is a list that contains only the words from the "unique_words" set that have more than 5 characters.
# "len" is a built-in function in Python that returns the length of a string. In this case, it is used to check if the length of each word is greater than 5.
long_words = [word for word in unique_words if len(word) > 5]

print(long_words)

# script to run the text analyser: python day-11_The_Text_Analyser.py