# List with all of the temperatures for the week.
# '68, 82, 71...' are integerstemps = [68, 82, 71, 89, 74, 81, 65]
temps = [68, 82, 71, 89, 74, 81, 65]

def filter_hot_days(temperatures, threshold=75):
	return [temp for temp in temperatures if temp > threshold]


def main():
	hot_days = filter_hot_days(temps)
	print(f"Temperatures over 75: {hot_days}")
	print(f"Hot days: {len(hot_days)}")


if __name__ == "__main__":
	main()

# script to run the code: python list_filtering.py