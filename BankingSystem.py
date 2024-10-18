#Develop a banking system where the user can create and account, deposit money, withdraw money, and check their balance. Use classes to represent the account and its methods.
#
#Sample output:
#Options: deposit, withdraw, check balance, exit
#What would you like to do? deposit
#Enter amount to deposit: 500
#Deposited: $500.00.  New Balance: $500.00.

acc = 0

def create():
  global acc
  print("Account created. Account Id: 12345")

def deposit():
  global acc
  
  amount = int(input("Enter amount to deposit:"))
  acc = acc + amount
  print("Deposited: $" + str(amount) + ",New Balance: $" + str(acc))
  
def withdraw():
  global acc
  
  withdrawAmount = int(input("Enter amount to be withdrawed:"))
  acc = acc + withdrawAmount
  print("withdrawAmount: $" + str(withdrawAmount) + ",New Balance: $" + str(acc))

def checkBalance():
  global acc
  
  print("Current balance: ", acc)
  

print("Options: Create, Deposit, Withdraw, Check balance, Exit")

options = input("What would you like to do?")

if options == "Deposit":
  deposit()
elif options == "Create":
  create()
elif options == "Withdraw":
  withdraw()
elif options == "Check balance":
  checkBalance()
elif options == "exit":
  exit()
else:
  print("Please choose a valid option")
