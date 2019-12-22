#! old for loop - for (var i = 0; i < 10; i++)



for i in range(11):
    print (i)
print("Rob")

#! To add a starting number just put in another parameter
for i in range(5,11):
    print (i)

favFoods = ["ice cream", "cake", "seafood"]

for i in favFoods:
    print ("I like eating " + i)


#! While loops

x = 0
while x <= 10:
    print (x)
    x += 1
    
# Create dictionary containing 4 names and ages of people
# Create a loop that prints the age for each person
    
friends = {}
friends["Joe"] = 31
friends["John"] = 32
friends["Josh"] = 33

for age in friends:
    print (age + " is " + str(friends[age]))
    



