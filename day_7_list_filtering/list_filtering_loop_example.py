temps = [68, 82, 71, 89, 74, 81, 65]

def filter_hot_days(temperatures, threshold=75):
    hot_days = []
    for temp in temperatures:
        if temp > threshold:
            hot_days.append(temp)
    return hot_days


def main():
    hot_days = filter_hot_days(temps)
    print(f"Temperatures over 75: {hot_days}")
    print(f"Hot days: {len(hot_days)}")


if __name__ == "__main__":
    main()

# script to run the code: python list_filtering_loop_example.py