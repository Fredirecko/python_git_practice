#Polymorphism exercise


class Square():
    def __init__(self,side):
        self.side = side
    def __pow__(squareOne,squareTwo):
        return(squareOne.side**squareTwo.side)
    
    
squareOne = Square(10)
squareTwo= Square(2)



print("The square of squareOne raised by squareTwo is: ", squareOne**squareTwo)