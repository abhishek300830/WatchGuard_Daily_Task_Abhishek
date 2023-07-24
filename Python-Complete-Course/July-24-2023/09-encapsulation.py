class Base:
    def __init__(self):
        self.public = 10
        self.__private =20

class Child(Base):
    def __init__(self):
        super().__init__()
        # calling private of base class
        # print(self.__private)


object = Base()
print(object.public)

child = Child()
print(child.__class__)