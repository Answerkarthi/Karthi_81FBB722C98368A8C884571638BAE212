class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          return f"${amount} deposited successfully."
      else:
          return "Invalid deposit amount."

  def withdraw(self, amount):
      if amount > 0 and self.__account_balance >= amount:
          self.__account_balance -= amount
          return f"${amount} withdrawn successfully."
      else:
          return "Insufficient funds or invalid withdrawal amount."

  def display_balance(self):
      return f"Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder_name}\nAccount Balance: ${self.__account_balance:.2f}"

# Creating an instance of the BankAccount class
account = BankAccount("1234567890", "leo das", 5000.0)

# Testing deposit and withdrawal functionality
print(account.display_balance())  # Display initial balance
print(account.deposit(500.50))    # Deposit $500.50
print(account.withdraw(200.75))   # Withdraw $200.75
print(account.display_balance())  # Display updated balance
