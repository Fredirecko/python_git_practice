 #Object Orienting Programming
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

#Hello World 

print("Hello World!")

#Classes and Objects
#Classes - logical collection of attributes and methods
#Objects - instances of a class

# Noun=>Class  Adjective=>Attributes  Verb=>Method

#Example - check if an employee has achieved his weekly target or not
#Class
class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6
    
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Targe has been achieved")
        else:
            print("Targe has not been achieved")

# Object
employeeOne = Employee()
employeeOne.name

#Class Example
class Business:
    numberOfWorkingHours = 40
    

# Create Object of Class Business

employeeSam = Business()
employeeJoe = Business()

# Changing a Class Attribute - ex: change number of working hours from 40 to 45

Business.numberOfWorkingHours = 45

# An Instance Attribute is an attribute that is specific to each instance of your Class
employeeJoe.name = "John"

    
    
    
    
    
    
    
    
    
    
    
    


