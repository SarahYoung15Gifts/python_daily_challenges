def get_median(data_list):
	# Sort numbers from smallest to largest first.
	data_list.sort()

	if not data_list:
		raise ValueError("data_list cannot be empty")

# "size" is the number of items in the list, and "middle_index" is the index of the middle item.
	size = len(data_list)
	middle_index = size // 2

# If the list has an odd number of items, return the middle one. If it has an even number of items, return the average of the two middle ones.
	if len(data_list) % 2 != 0:
		return data_list[middle_index]

	return (data_list[middle_index - 1] + data_list[middle_index]) / 2


def main():
	list_a = [10, 2, 38, 23, 38, 23, 21]
	list_b = [10, 2, 38, 23, 38, 23]

	print(f"Median for list a: {get_median(list_a)}")  # Output: Median for list a: 23
	print(f"Median for list b: {get_median(list_b)}")  # Output: Median for list b: 23.0


if __name__ == "__main__":
	main()

# Run in terminal with: python day_16_the_data_sanitiser.py