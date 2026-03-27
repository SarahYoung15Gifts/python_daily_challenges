# Here we are defining a function called calculate_trip_cost that takes three parameters: miles, mpg, and price_per_gallon. 
# Then it calculates the total cost of the trip by multiplying the gallons needed by the price per gallon.
def calculate_trip_cost(miles, mpg, price_per_gallon):
	# The function calculates the number of gallons needed for the trip by dividing the miles by the miles per gallon (mpg). 
	gallons_needed = miles / mpg
	# Then it calculates the total cost of the trip by multiplying the gallons needed by the price per gallon.
	total_cost = gallons_needed * price_per_gallon
	#Finally, it returns the total cost.
	return total_cost

# float() is used to convert the user input from a string to a floating-point number, which allows for decimal values.
miles = float(input("Enter miles: "))
mpg = float(input("Enter mpg: "))
price_per_gallon = float(input("Enter price per gallon: "))

# We call the calculate_trip_cost function with the user inputs and store the result in the variable trip_cost.
trip_cost = calculate_trip_cost(miles, mpg, price_per_gallon)

# Finally, we print the trip cost formatted to two decimal places. The :.2f format specifier ensures that the output is displayed with two digits after the decimal point, which is common for currency values.
print(f"Trip cost: ${trip_cost:.2f}")