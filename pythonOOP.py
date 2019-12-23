#Object Orienting Programming
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

#Hello World 

print("Hello World!")

#Classes and Objects
#Classes - logical collection of attributes and methods
#Objects - instances of class

# Noun=>Class  Adjective=>Attributes  Verb=>Method

#Example - check if an employee has achieved his weekly target or not

class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6
    
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Targe has been achieved")
        else:
            print("Targe has not been achieved")

employeeOne = Employee()
employeeOne.name


