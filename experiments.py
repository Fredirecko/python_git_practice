#test


#Test 1 - sending results of a method from one class to the empty variables of another classes function



class Form:
    
    def signUpForm(self):
        
        print(" ")
        print("What is your name?")
        print(" ")
        self.name = input()
        
        print(" ")
        print("What is your favorite color?")
        print(" ")
        self.favoriteColor = input()
        
        print(" ")
        print("What is your favorite number?")
        print(" ")
        self.favoriteNumber = int(input())
        
        print(" ")
        print("What is your password?")
        print(" ")
        self.password = input()
        
        newUserInfo = ["Name: {}".format(self.name),"Favorite color: {}".format(self.favoriteColor),"Favorite number: {}".format(self.favoriteNumber),"Password: {}".format(self.password)]
        
        return newUserInfo 

class Profile:
    
    
    
    def newProfile(self,userInfo):
        
        self.newProfileDetails = userInfo
        
        for detail in self.newProfileDetails:
            print(detail)
        
        print(self.newProfileDetails)
        




newUser = Form()
user = Profile()

userInfo = newUser.signUpForm()
user.newProfile(userInfo)



