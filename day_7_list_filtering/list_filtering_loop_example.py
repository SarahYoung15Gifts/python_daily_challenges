temps = [68, 82, 71, 89, 74, 81, 65]

hot_days = []
for temp in temps:
    if temp > 75:
        # 'append' is a method that adds an item to the end of a list. In this case, it adds the temperature 'temp' to the 'hot_days' list if it is greater than 75.
        hot_days.append(temp)

print(f"Temperatures over 75: {hot_days}")

print(f"Hot days: {len(hot_days)}")

# script to run the code: python list_filtering_loop_example.py