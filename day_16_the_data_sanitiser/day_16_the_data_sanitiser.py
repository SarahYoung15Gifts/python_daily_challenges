def get_median(data_list):
	if not data_list:
		raise ValueError("data_list cannot be empty")

	# Sort numbers from smallest to largest first.
	sorted_data = sorted(data_list)

# "size" is the number of items in the list, and "middle_index" is the index of the middle item.
	size = len(sorted_data)
	middle_index = size // 2

# If the list has an odd number of items, return the middle one. If it has an even number of items, return the average of the two middle ones.
	if len(sorted_data) % 2 != 0:
		return sorted_data[middle_index]

	return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2


def build_median_messages(list_a, list_b):
	return [
		f"Median for list a: {get_median(list_a)}",
		f"Median for list b: {get_median(list_b)}",
	]


def main():
	list_a = [10, 2, 38, 23, 38, 23, 21]
	list_b = [10, 2, 38, 23, 38, 23]

	for message in build_median_messages(list_a, list_b):
		print(message)


if __name__ == "__main__":
	main()

# Run in terminal with: python day_16_the_data_sanitiser.py