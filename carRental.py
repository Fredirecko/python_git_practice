class Company:
    def __init__(self):
        self.carTypes = ["1. Hatchback @ $30/day", "2. Sedan @ $50/day", "3. SUV @ $100/day"]
        
        self.hatchback = "hatchback"
        self.sedan = "sedan"
        self.suv = "SUV"
        
        self.chosenType = ""
        self.cost = 0
        self.rentalDuration = 0
    
    def typeOfCar(self):
        for car in self.carTypes:
            print(car)
    
    def rentalHatchback(self):
        
        print("")
        print("Great! You picked a hatchback. Hatchbacks cost $30 per day.")
        print("")
        print("How many days would you like to rent your vehicle?")
        print("(Enter a whole number)")
        self.days = int(input())
        return self.days
        print("")
        
    def costOfRentalHatchback(self,days):
        
        self.days = days
        self.hatchbackCost = 30
        
        self.totalCost = self.days * self.hatchbackCost
        
        print("Your total cost to rent a hatchback for " + str(self.days) + " day(s)" + " will be " + "$" + str(self.totalCost) + ".")
        
    
    def rentalSedan(self):
        
        print("")
        print("Great! You picked a sedan. Sedans cost $50 per day.")
        print("")
        print("How many days would you like to rent your vehicle?")
        print("(Enter a whole number)")
        self.days = int(input())
        return self.days
        print("")
        
    def costOfRentalSedan(self,days):
        
        self.days = days
        self.sedanCost = 50
        
        self.totalCost = self.days * self.sedanCost
        
        print("Your total cost to rent a sedan for " + str(self.days) + " day(s)" + " will be " + "$" + str(self.totalCost) + ".")
    
    def rentalSUV(self):
        
        print("")
        print("Great! You picked an SUV. SUV's cost $100 per day.")
        print("")
        print("How many days would you like to rent your vehicle?")
        print("(Enter a whole number)")
        self.days = int(input())
        return self.days
        print("")
        
    def costOfRentalSUV(self,days):
        
        self.days = days
        self.suvCost = 100
        
        self.totalCost = self.days * self.suvCost
        print("Your total cost to rent an SUV for " + str(self.days) + " day(s)" + " will be " + "$" + str(self.totalCost) + ".")
        
    def rentalDetails(self):
        
        print("Fantasic! Enjoy your rental vehicle and please drive safe.")
    
    
staff = Company()

while True:
    print("")
    print("Hello! Welcome to Car Rental Deluxe")
    print("What type of car would you like to rent?")
    print("")
    staff.typeOfCar()
    print("")
    print("Enter a number corresponding to the type of car")
    userInput = int(input())

    if userInput == 1:
        days = staff.rentalHatchback()
        staff.costOfRentalHatchback(days)
    elif userInput == 2:
        days = staff.rentalSedan()
        staff.costOfRentalSedan(days)
    elif userInput == 3:
        days = staff.rentalSUV()
        staff.costOfRentalSUV(days)
    else: 
        print("Invalid input. Try again.")


    print("")
    print("Press 1 to confirm rental.")
    print("Press 2 to restart/change rental choice.")
    print("Press 3 to quit program.")
    print("")
    
    userInput = int(input())
    
    if userInput == 1:
        staff.rentalDetails()
        quit()
    elif userInput == 2:
        pass
    elif userInput == 3:
        quit()
    else: 
        print("Invalid input. Try again.")





