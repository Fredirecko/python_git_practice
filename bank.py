#Banking System

#Details that need to be included
# Give prompt to the user asking if they wish to Create A New Account or Access Existing Account
# New Account - accept name, initial deposit, and create random 5 digit account number
# Existing Account - accept name and account number to validate user. Options to withdraw, deposit or check balance




class Bank:
    
    def newAccount(self):
    
        self.accountNumber = random.randint(10000,100000)

        print(" ")
        print("Enter Name: ")
        print(" ")
        self.name = input()

        print(" ")
        print("Initial Deposit: ")
        print(" ")
        self.deposit = int(input())

        print(" ")
        print("Here is your new account number: {}. Please write it down.".format(self.accountNumber))
        print(" ")

        self.accountDetails = [self.name, self.deposit, self.accountNumber]
        
        return self.accountDetails
    
    def existingAccount(self, newDetails):
        
        self.accountInformation = newDetails
        
        #if statement validating user which runs for loop displaying account details
        print(" ")
        print("What is your name?")
        print(" ")
        self.validation = input()
        
        if self.validation != self.accountInformation[0]:
            print(" ")
            print("Sorry please try again.")
            print(" ")
        else:
            print(" ")
            print("Name: {}".format(self.accountInformation[0]))
            print(" ")
            print(" ")
            print("Balance: {}".format(self.accountInformation[1]))
            print(" ")
            print(" ")
            print("Account Number: {}".format(self.accountInformation[2]))
            print(" ")
            print(" ")
            
            while True:
                print("Enter 1 to withdraw.")
                print("Enter 2 to deposit.")
                print("Enter 3 to exit.")
                print(" ")
            
                self.inputHere = int(input())
                if self.inputHere == 1:
                    print(" ")
                    print("Enter amount to withdraw: ")
                    amount = int(input())
                    if amount > self.accountInformation[1]:
                        print(" ")
                        print("I'm sorry that amount exceeds your current balance.")
                        print(" ")
                    else:
                        self.accountInformation[1] = amount
                        print(" ")
                        print("Your amount has been transferred. Thank you!")
                        print(" ")
                    print(" ")
                elif self.inputHere == 2:
                    pass
                elif self.inputHere == 3:
                    quit()
                else:
                    print(" ")
                    print("Please enter a valid input. Thank you.")
                    print(" ")
            
            
        #Once account details displayed have menu ask for actions: withdraw, deposit, view balance


import random

user = Bank()

print(" ")
print("Welcome to the banking system.")
print(" ")

while True:
    
    print(" ")
    print("Enter 1: Create new account")
    print(" ")
    print(" ")
    print("Enter 2: Access existing account")
    print(" ")
    print(" ")
    print("Enter 3: Quit")
    print(" ")
    
    newOrExisting = int(input())

    if newOrExisting == 1:
        newDetails = user.newAccount()
    elif newOrExisting == 2:
        user.existingAccount(newDetails)
    elif newOrExisting == 3:
        quit()
    elif newOrExisting != 1 or 2 or 3:
        print(" ")
        print("Please enter a valid input. Thank you.")
        print(" ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



