"""This class represents an animal and its behaviors. It has attributes for the
animal's name, what it eats, and the sound it makes. The class also has methods
to print out the animal's eating habits and the sound it makes."""

class Animal: #this is the parent class
    def __init__(self, name, feed, sound):  #this is the constructor method that initializes the attributes of the class
        self.name = name #this is a public attribute that can be accessed from outside the class
        self.feed = feed #this is a public attribute that can be accessed from outside the class
        self.sound = sound #this is a public attribute that can be accessed from outside the class

    def eat(self): #this is a method that prints out what the animal eats
        print(f"{self.name} eats {self.feed}.") #this is a formatted string that prints out the animal's name and what it eats

    def make_sound(self): #this is a method that prints out the sound the animal makes
        print(f"{self.name} {self.sound}") #this is a formatted string that prints out the animal's name and the sound it makes

class Lion(Animal): #this is a child class that inherits from the Animal class
    def __init__(self, name): #this is the constructor method that initializes the attributes of the class
        super().__init__(name, "fresh meat", "roars loudly!")  #this calls the constructor of the parent class and passes in the name, feed, and sound attributes specific to a lion


class Elephant(Animal): #this is a child class that inherits from the Animal class
    def __init__(self, name): #this is the constructor method that initializes the attributes of the class
        super().__init__(name, "grass and fruits", "trumpets!") #this calls the constructor of the parent class and passes in the name, feed, and sound attributes specific to an elephant 

class Monkey(Animal): #this is a child class that inherits from the Animal class
    def __init__(self, name): #this is the constructor method that initializes the attributes of the class
        super().__init__(name, "bananas", "chatters!") #this calls the constructor of the parent class and passes in the name, feed, and sound attributes specific to a monkey


lion = Lion("Simba") #this creates an instance of the Lion class with the name "Simba"
elephant = Elephant("Dumbo") #this creates an instance of the Elephant class with the name "Dumbo"
monkey = Monkey("George") #this creates an instance of the Monkey class with the name "George"

lion.make_sound() #this calls the make_sound() method of the Lion class, which prints out the sound the lion makes
lion.eat() #this calls the eat() method of the Lion class, which prints out what the lion eats
print("------------------------------") #format thingy
elephant.make_sound() #this calls the make_sound() method of the Elephant class, which prints out the sound the elephant makes
elephant.eat() #this calls the eat() method of the Elephant class, which prints out what the elephant eats
print("------------------------------") #format thingy
monkey.make_sound() #this calls the make_sound() method of the Monkey class, which prints out the sound the monkey makes
monkey.eat() #this calls the eat() method of the Monkey class, which prints out what the monkey eats

#this code is pasted from vs code
