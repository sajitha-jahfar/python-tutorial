# class Car:
#     def __init__(self,brand,color,year):
#         self.brand=brand
#         self.color=color
#         self.year=year
#     def display_info(self):
#         print(f"brand:{self.brand} color:{self.color} year:{self.year}")
# car1=Car("toyota","blue",2000)
# car1.display_info()
# print(car1.color)  #accessing particular atribute
# car1.brand="bmw" #modifying an atribute value
# car1.display_info() #calling a method

class Dog:
    def __init__(self,color,breed):
        self.breed=breed
        self.color=color
    def bark(self):
        print(f"{self.color} colored {self.breed} barks")
  

dog1=Dog("white","bulldog")
dog2=Dog("black","german shepherd")
dog1.bark()
dog2.bark()
dog1.breed="doberman"
dog1.bark()