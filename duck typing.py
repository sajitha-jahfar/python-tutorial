
class Cat:
    def speak(self):
        print("moew")

class Dog:
    def speak(self):
        print("Bark!")

def make_sound(animal):
    animal.speak()   # Python only checks if 'speak()' exists

d = Dog()
c = Cat()

make_sound(d)
make_sound(g)
