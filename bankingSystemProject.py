#Banking System

#Details that need to be included
# Give prompt to the user asking if they wish to Create A New Account or Access Existing Account
# New Account - accept name, initial deposit, and create random 5 digit account number
# Existing Account - accept name and account number to validate user. Options to withdraw, deposit or check balance

class Bank:
    
    def __init__(self):
        
        existingAccountNumbers = {}
    
    def newAccount(self):
        
        self.firstName = ""
        self.lastName = ""
        self.newDeposit = 0.0
        self.accountNumber = random.randint(10000,100000)
        self.accountCreated = "Congratulations {}, you have created a new account!".format(self.firstName)
        
        print(" ")
        print("Hi, I'm Whimsy! We are glad you have chosen The New Bank of Sky Kingdom.  You can trust us with guarding your treasure as we have 24 hour Wizard Surveillance and Dragon level security. Our vault is fashioned from the best dwarf technology. Let's get started with setting up your account, shall we?")
        print(" ")
        
        print(" ")
        print("Please enter your first name.")
        print(" ")
        self.firstName = input()
        print(" ")
        print("Please enter your last name.")
        print(" ")
        self.firstName = input()
        print(" ")
        print("Please enter the amount of your initial deposit.")
        print(" ")
        self.firstName = float(input())
        print(" ")
        print("Thank you.  Here is your account number. Please memorize it.", self.accountNumber)
        print(" ")
        
        
          
    def existingAccount(self):
        
        print(" ")
        print("Welcome back loyal patron!  We just need you to verify a few details before we give you access to the vault.")
        print(" ")
    
    def deposit(self,name,deposit):
        
        self.name = name
        self.deposit = newDeposit
        self.accountNumber = accountNumber
    
    def withdrawal(self):
        pass


class AccountHolder(Bank):
    
    def Account(self):
        print(" ")
        print("Account Holder: {} {}. Account Number: {} Account Total: {}".format(self.firstName, self.lastName, self.newDeposit, self.accountNumber))
        print(" ")
    
    def accountBalance(self):
        pass


    
import random

bank = Bank()
patron = AccountHolder()
    
#
#-----Introduction-----
#
print(" ")
print("Welcome to the New Bank of Sky Kingdom.")
print(" ")

#
#-----Existing or New?------
#
print(" ")
print("Are you an existing account holder or would you like to set up a new account?")
print(" ")

print(" ")
print("Enter 1 for existing account holder.")
print("Enter 2 to set up a new account.")
print(" ")

while True:
    newOrExisting = int(input())

    if newOrExisting == 1:
        pass
    elif newOrExisting == 2:
        bank.newAccount()
    else:
        print(" ")
        print("Please enter a valid input. Thank you.")
        print(" ")
        
    



    
    
    
