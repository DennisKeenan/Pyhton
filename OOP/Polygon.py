from abc import ABC,abstractmethod

class Polygon (ABC):
    @abstractmethod
    def nosides(self):
        pass
    @abstractmethod
    def getarea(self):
        pass

class Triangle (Polygon):
    def __init__(self,base:float,height:float) -> None:
        self.base=base
        self.height=height
    def getarea (self):
        return 0.5*self.base*self.height
    def nosides(self):
        print("I have 3 sides")

class Rectangle (Polygon):
    def __init__(self,length:float,width:float) -> None:
        self.length=length
        self.width=width
    def getarea (self):
        return self.length*self.width
    def nosides(self):
        print("I have 4 sides")

Triangle1=Triangle(3,3)
Rectangle1=Rectangle(5,9)
print(Triangle1.getarea())
print(Rectangle1.getarea())