from abc import ABC,abstractmethod


class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle:
    def no_of_sides(self):
        print("i have 3 sides")

class Square:
    def no_of_sides(self):
        print("i have 4 sides")

square = Square()
square.no_of_sides()

triangle =  Triangle()
triangle.no_of_sides()