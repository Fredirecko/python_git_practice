
#Inheritance Exercise 
#created by Febin George
# EXERCISE - INHERITANCE
# Write an object oriented program that performs the following tasks:
# 1. Create a class called Chair from the base class Furniture
# 2. Teakwood should be the type of furniture that is used by all furnitures by default
# 3. The user can be given an option to change the type of wood used for chair if he wishes to
# 4. The number of legs of a chair should be a property that should not be altered outside the class

class Furniture:
        primaryWoodType = "Teakwood"
        secondaryMaterial = ["1. Teakwood (default)", "2. Oak", "3. Elm", "4. Birch", "5. Mahagony", "6. Aluminum", "7. Steel", "8. Plastic", "9. Kevlar"]
        sizeOfFurniture = ["1. Small", "2. Medium", "3. Large"]

class Chair(Furniture):
    
    def __init__(self):
        self._numberOfLegs = 4
        
    
    def sizes(self):
        
        self.size = ""
        
        print(" ")
        print(" ")
        print("Enter the number corresponding to the size of furniture you wish to order.")
        for sizes in self.sizeOfFurniture:
            print(sizes)
        
        self.chairSize = int(input())
        print(" ")
        
        if self.chairSize == 1:
            print("You chose small.")
            self.size = "small"
        elif self.chairSize == 2:
            print("You chose medium.")
            self.size = "medium"
        elif self.chairSize == 3:
            print("You chose large.")
            self.size = "large"
        
        return self.size
        print(" ")
        
    def material(self):
        
        self.materials = ""
        
        print(" ")
        print(" ")
        print("All chairs are by default constructed from Teakwood. If you would like to choose a different material please select from the options below. Enter the number corresponding to the material of furniture you wish to order.")
        print(" ")
        print(" ")
        
        for material in self.secondaryMaterial:
            print(material)
            
        self.materialOption = int(input())
        print(" ")
        
        if self.materialOption == 1:
            print("You chose Teakwood (default).")
            self.materials = "teakwood"
        elif self.materialOption == 2:
            print("You chose oak.")
            self.materials = "oak"
        elif self.materialOption == 3:
            print("You chose elm.")
            self.materials = "elm"
        elif self.materialOption == 4:
            print("You chose birch.")
            self.materials = "birch"
        elif self.materialOption == 5:
            print("You chose mahagony.")
            self.materials = "mahagony"
        elif self.materialOption == 6:
            print("You chose aluminum.")
            self.materials = "aluminum"
        elif self.materialOption == 7:
            print("You chose steel.")
            self.materials = "steel"
        elif self.materialOption == 8:
            print("You chose plastic.")
            self.materials = "plastic"
        elif self.materialOption == 9:
            print("You chose kevlar.")
            self.materials = "kevlar"
        
        return self.materials
        print(" ")
        
    
    def orderConfirmation(self, chairSize, materialType):
        
        self.chairSize = chairSize
        self.materialType = materialType
        
        print(" ")
        print(" ")
        print("You have ordered a {} chair made of {}.".format(self.chairSize,self.materialType))
        print(" ")
        print(" ")
        print("If this is correct press 1 to confirm order and exit. If you would like to return to main menu to restart or exit, press 2.")
        print(" ")
        print(" ")
        customerConfirmation = int(input())
        if customerConfirmation == 1:
            "Thank you for your order!"
            quit()
        elif customerConfirmation == 2:
            pass
    
chairOrder = Chair()
chairSize = "" 
materialType = ""

print(" ")
print(" ")
print("Hi! Welcome to the chair ordering terminal. Please select from the following options to place your chair order.")

while True:
    print(" ")
    print(" ")
    print("Enter 1 to choose size of chair.")
    print("Enter 2 to choose type of material for chair construction.")
    print("Enter 3 to confirm order")
    print("Enter 4 to restart order")
    print("Enter 5 to exit.")

    customerInput = int(input())

    if customerInput == 1:
        chairSize = chairOrder.sizes()
    elif customerInput == 2:
        materialType = chairOrder.material()
    elif customerInput == 3:
        if chairSize == "" or materialType == "":
            print("Make sure you have first chosen a chair size and chosen your chair material type. Thanks.")
        else:
            chairOrder.orderConfirmation(chairSize,materialType)
    elif customerInput == 4:
        pass
    elif customerInput == 5:
        quit()
    else:
        print(" ")
        print(" ")
        print("Invalid input. Please try again.")
        print(" ")
        print(" ")
        

    








