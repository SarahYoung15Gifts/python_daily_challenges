# Here we are defining a function called calculate_trip_cost that takes three parameters: miles, mpg, and price_per_gallon. 
# Then it calculates the total cost of the trip by multiplying the gallons needed by the price per gallon.
def calculate_trip_cost(miles, mpg, price_per_gallon):
	# The function calculates the number of gallons needed for the trip by dividing the miles by the miles per gallon (mpg). 
	gallons_needed = miles / mpg
	# Then it calculates the total cost of the trip by multiplying the gallons needed by the price per gallon.
	total_cost = gallons_needed * price_per_gallon
	#Finally, it returns the total cost.
	return total_cost

def format_trip_cost(total_cost):
	return f"Trip cost: ${total_cost:.2f}"


def run_trip_calculator(reader=None, writer=None):
	reader = reader or input
	writer = writer or print
	miles = float(reader("Enter miles: "))
	mpg = float(reader("Enter mpg: "))
	price_per_gallon = float(reader("Enter price per gallon: "))
	trip_cost = calculate_trip_cost(miles, mpg, price_per_gallon)
	writer(format_trip_cost(trip_cost))


def main():
	run_trip_calculator()


if __name__ == "__main__":
	main()