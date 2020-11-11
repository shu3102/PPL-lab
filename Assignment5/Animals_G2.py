class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes

class wild_animals(Animals):
    def place(self):
        print("Forests")

class carnivores(wild_animals):
    def food(self):
        print("Meat")

class tiger(carnivores):
    def speak(self):
        print("Chuff")
    def colour(self):
        print("Orange, White, Brown")

class lion(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellow, Brown")

class hyena(carnivores):
    def speak(self):
        print("Laugh")
    def colour(self):
        print("Grey, Brown")

class herbivores(wild_animals):
    def food(self):
        print("Plants")

class deer(herbivores):
    def speak(self):
        print("Bellow, Bleat")
    def colour(self):
        print("Brown")

class elephant(herbivores):
    def speak(self):
        print("Trumpet")
    def colour(self):
        print("Grey")

class zebra(herbivores):
    def speak(self):
        print("Neigh, Whinny, Nicker")
    def colour(self):
        print("Black and White")

class domestic_animals(Animals):
    def place(self):
        print("Areas habitated by human beings")

class dog(domestic_animals, carnivores):
    def speak(self):
        print("Bark")
    def colour(self):
        print("Brown, Black, White")

class cat(domestic_animals, carnivores):
    def speak(self):
        print("Meow")
    def colour(self):
        print("Brown, Black, White")

class cow(domestic_animals, herbivores):
    def speak(self):
        print("Moo")
    def colour(self):
        print("White, Brown")

class buffalo(domestic_animals, herbivores):
    def speak(self):
        print("Grunt")
    def colour(self):
        print("Black, Brown")

class goat(domestic_animals, herbivores):
    def speak(self):
        print("Bleat")
    def colour(self):
        print("Black, Brown, Grey")



# tiger
print("Tiger: ")
a1 = tiger(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# lion
print("Lion: ")
a1 = lion(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# hyena
print("Hyena: ")
a1 = hyena(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# deer
print("Deer: ")
a1 = deer(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# elephant
print("Elephant: ")
a1 = elephant(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# zebra
print("Zebra: ")
a1 = zebra(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# dog
print("Dog: ")
a1 = dog(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# cat
print("Cat: ")
a1 = cat(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# buffalo
print("Buffalo: ")
a1 = buffalo(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")

# goat
print("Goat: ")
a1 = goat(4,2)
a1.place()
a1.colour()
a1.speak()
a1.food()
print("\n")