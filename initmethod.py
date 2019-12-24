#init method practice


class Employee:

# Use __init__ to initial attributes so that when methods are called you don't run into errors
    def __init__(self, name):
        self.name = name
    
        
    def displayEmployeeDetails(self):
        print(self.name)
        
        
employee = Employee("Mark")
employeeTwo = Employee("Matthew")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()


