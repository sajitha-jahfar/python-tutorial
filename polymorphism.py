class Animal:
    # def __init__(self,name):
    #     self.name=name
    def sound(self):
        print(" making sound")

class Dog(Animal):
    def sound(self):
        print(" dog says bow bow")
class Cat(Animal):
     def sound(self):
        print(" cat says meow")
def animal_sound(animal):
    animal.sound()

d=Dog()
c=Cat()
animal_sound(d)
animal_sound(c)
