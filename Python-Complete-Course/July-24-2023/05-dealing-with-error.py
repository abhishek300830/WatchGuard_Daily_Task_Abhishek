class Car:
    def __init__(self , make ,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_cars(self,car):
        if not isinstance(car , Car):
            raise TypeError(f"Tried to add {car.__class__.__name__} which is not object of Car")
        self.cars.append(car)
    
ford = Garage()
car = Car("Ford", "Fiesta")

try:
    ford.add_cars(car) # run properly
    ford.add_cars("he") # exception caught
    print("car is added")
except TypeError:
    print("your car is not a car.")
except ValueError:
    print('value error occured')
finally:
    print("i will always run")