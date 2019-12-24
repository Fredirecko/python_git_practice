#Precious Stone Game
#Create a class PreciousStones, a class Pouch and a class Search
#Create a method in PreciousStones that generates a random stone
#Create a method in Pouch that stores acquired stones
#Create a method in class Search that generates a random precious stone or returns "Stone not found"



class SearchPreciousStones:
    
    def __init__(self):
        self.diamond = "Diamond"
        self.ruby = "Ruby"
        self.sapphire = "Saphire"
        self.emerald = "Emerald"
        self.tourmaline = "Tourmaline"
        self.opal = "Opal"
        self.aquamarine = "Aquamarine"
        self.topaz = "Topaz"
        self.amethyst = "Amethyst"
        self.lapisLazuli = "Lapis Lazuli"
        self.onyx = "Onyx"
        self.jade = "Jade"
        self.alexandrite = "Alexandrite"
        self.heliodor = "Heliodor"
        self.garnet = "Garnet"
        self.citrine = "Citrine"
        
        self.preciousStones = ["Diamond", "Ruby", "Sapphire", "Emerald", "Tourmaline", "Opal", "Aquamarine", "Topaz", "Amethyst", "Lapis Lazuli", "Onyx", "Jade", "Alexandrite", "Heliodor", "Garnet", "Citrine"]
        
        self.pouch = []
    
    def search(self):
        
        self.searchSuccess = random.randint(0,1)
        self.foundStone = random.choice(self.preciousStones)
        
        if self.searchSuccess == 1:
            print("You found a precious stone: " + self.foundStone)
            self.pouch.append(self.foundStone)
        else:
            print("You're search failed. Please try again.")
            
    def examinePouch(self):
        
        print(self.pouch)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        