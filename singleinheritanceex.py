
#single inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} making sound")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} says bow bow")

d=Dog("johny")
d.sound()


