#functin practice

# use def to define a function

def hello():
    print ("Hello!")
    
hello()

def saySomething(something):
    print(something + "!")
    
saySomething("I like apples")

def addNumbers(x,y):
    return x+y
    
print(addNumbers(1034,897))

# Create function called highestCommonFactor which returns the highest number that
#divides into two other numbers exactly

def highestCommonFactor(x,y):
    for i in range(1,x+1):
        if x % i==0 and y%i == 0:
            hcf = i
    return hcf

print(highestCommonFactor(503,895))


a=5
b=6

def addTwoNumbers():
    a=10
    return a+b

print(addTwoNumbers())




