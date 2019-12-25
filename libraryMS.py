#Implement Library Management System
#Customer should be able to display all the books available in the library
#Handle the process when a customer requests to borrow a book
#Update the library collection when the customer returns a book

class Library:
    
    def __init__(self):
        self.bookTitles = ["Moby Dick", "The Count of Monte Cristo", "Little Dorrit", "Dune", "20,000 Leagues Under The Sea", "The Hobbit", "Roots of Strategy", "East of Eden", "Grapes of Wrath", "Tortilla Flats", "Oliver Twist", "Great Expectations"]
    
    def requestAllTitles(self):
        
        print(self.bookTitles)
        
    def searchBookTitle(self, title):
        
        self.title = title
        
        if self.title in self.bookTitles:
            print("We have " + self.title)
        else:
            print("We do not have that title.")
            
    def borrowBook(self,title):
        self.title = title
        
        if self.title in self.bookTitles:
            self.bookTitles.remove(self.title)
            print("You have checked out " + self.title + "." + "You have five days to return it. Enjoy!")
        else:
            print("Sorry, we do not have that title in the library at this time.")
            
    def returnBook(self,title):
        self.title = title
        
        self.bookTitles.append(self.title)
        print("Thank you for returning " + self.title + "!")
        
        















