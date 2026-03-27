# "text" is a string variable that contains a sample text for analysis.
text = "Python is amazing and Python is fun to learn. Learning Python opens many doors for a programmer."

def analyze_text(value):
	normalized_text = value.lower().replace(".", "")
	words = normalized_text.split()
	unique_words = set(words)
	return [word for word in unique_words if len(word) > 5]


def main():
	print(analyze_text(text))


if __name__ == "__main__":
	main()

# script to run the text analyser: python day_11_the_text_analyser.py