from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):Z
        return self.height*self.width
rectangle=Rectangle(10,20)
print(rectangle.area())