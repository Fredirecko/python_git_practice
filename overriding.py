# Polymorphism
# Overriding examples

class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40
        
    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

#created new class and named method the same as from class Employee thus overriding the previous numberOfWorkingHours
class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45
#the super() function is used to access the base class (in this case - Employee) 
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()
        
employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = " ")
employee.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = " ")
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset: ", end = " ")
trainee.displayNumberOfWorkingHours()

