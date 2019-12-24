#instance methods vs static methods

#instance methods make use of the self parameter to access and modify the instance attributes of class

class Employee:
    def employeeDetails(self):
        self.name = "Ben"

#Setting up a static method
    
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")
        
        
employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()







