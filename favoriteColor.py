#Simple program that asks for users favorite color based on a list of options
#Intent of program is to master user input function

class Color:
    
    
    
    def __init__(self):
        self.colors = ["1. Red","2. Orange","3. Yellow","4. Green","5. Blue","6. Purple","7. Violet","8. Grey"]
        
    def displayColorChoices(self):
        for color in self.colors:
            print(color)
        

colors = Color()
        
print("")
print("What is your favorite color?")
print("")
colors.displayColorChoices()
print("")
userChoice = input()
print("")
print(userChoice + " is a great color! Bye.")


