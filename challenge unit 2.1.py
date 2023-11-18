class BankAccount:
  def __init__(self, account_number, account_holder, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder = account_holder
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposit of ${amount:.2f} successful.")
      else:
          print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrawal of ${amount:.2f} successful.")
      else:
          print("Invalid withdrawal amount. Please check your balance and try again.")

  def display_balance(self):
      print(f"Account Number: {self.__account_number}")
      print(f"Account Holder: {self.__account_holder}")
      print(f"Account Balance: ${self.__account_balance:.2f}")


# Example usage:
# Create an instance of the BankAccount class
account = BankAccount(account_number="123456789", account_holder="John Doe", initial_balance=1000.0)

# Test deposit functionality
account.deposit(500.0)

# Test withdrawal functionality
account.withdraw(200.0)

# Display the account balance
account.display_balance()
