class BankAccount:

	def __init__(self, balance, username, pin):
		self.balance = balance
		self.username = username
		self.pin = pin
		self.disable = False
		self.wrong_entries = 0
		self.cooldown = 60
		self.deposit_limit = 1000

	def withdraw(self, amount):
		if self.disable == False: 
			user_pin = int(input("PIN: "))
			if user_pin == self.pin:
				if self.balance >= amount:
					self.balance -= amount
					print("You withdrew:", amount)
					print("Your current balance:", self.balance)
				else:
					print("Insufficient funds")
			else:
				print("INCORRECT PIN")
				self.wrong_entries += 1
				if self.wrong_entries > 3:
					self.disable = True

		else:
			print("ACCOUNT BLOCKED")

	def deposit(self, amount):
		

	def transfer(self, bank2, amount):








