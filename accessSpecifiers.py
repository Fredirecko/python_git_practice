# access specifiers

# Public => memberName
# Protected (acccesible to class and derived classes only) => _memberName **use one underscore**
# Private => __memberName **use two underscores**

class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017 # stored as _Car__yearOfManufacture
    
class BMW(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)
    
car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)

bmw = BMW()

print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)











