# a class is a blueprint of an object
class Animal():
    # constructor -- initializer - defining attributes of the class
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species

    def sound(self):
        print("I don't make a sound")

class Bird(Animal):
    def __init__(self, name, color, species, canFly):
        super().__init__(name, color, species)
        self.canFly = canFly

    def sound(self): #overwritting a method example of polymorphism
        print("tweet tweet")

class Fish(Animal):
    def __init__(self, name, color, species, freshWater):
        super().__init__(name, color, species)
        self.freshWater = freshWater
    
    def safeToPutInHomeTank(self):
        if self.freshWater:
            print("My name is", self.name,"Put me in the tank")
        else:
            print("My name is", self.name, "Put me in the ocean")


cat = Animal("felix", "brown", "feline")
dog = Animal("rover", "golden", "canine")
bird = Bird("tweety", "yellow", "avian", True)
fish = Fish("nemo", "orange", "clown fish", False)
Dory = Fish("Dory", "blue", "bluefish", False)


fish.safeToPutInHomeTank()
Dory.safeToPutInHomeTank()


# cat.sound()
# dog.sound()
# bird.sound()
# fish.sound()