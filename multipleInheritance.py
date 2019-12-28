#Inheritance practice

#Multiple Inheritance Practice

class OperatingSystem:
    multitasking = True
    name = "Mac OS"
    
class Apple:
    website="www.apple.com"
    name = "Apple"
    
class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Vist {} for more details".format(self.website))
            prin("Name: ", self.name)
            
            
macBook = MacBook()
            
    












