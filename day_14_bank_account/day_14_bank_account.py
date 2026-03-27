# Here we are creating a class called BankAccount.
class BankAccount:
	# The __init__ method is a special method that is called when an instance of the class is created. It initialises the attributes of the class.
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	# Here we are defining a method called deposit that takes an amount as an argument and adds it to the balance. 
    # It also prints a message indicating the deposit and the new balance.
	def deposit(self, amount):
		self.balance += amount
		print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

	# Here we are defining a method called withdraw that takes an amount as an argument and subtracts it from the balance if there are sufficient funds.
    # It also prints a message indicating the withdrawal and the new balance, or an error message if there are insufficient funds.
	def withdraw(self, amount):
		if amount > self.balance:
			print(f"{self.owner} attempted to withdraw ${amount}, but insufficient funds. Current balance: ${self.balance}")
		else:
			self.balance -= amount
			print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")


def main():
	# main part of the code where we create an instance of the BankAccount class..
	alice_account = BankAccount("Alice", 100)
	alice_account.deposit(50)
	alice_account.withdraw(20)
	alice_account.withdraw(200)

	bob_account = BankAccount("Bob", 200)
	bob_account.deposit(100)
	bob_account.withdraw(50)
	bob_account.deposit(100)
	bob_account.withdraw(300)


if __name__ == "__main__":
	main()

# script to run the code in the terminal: python day_14_bank_account.py

