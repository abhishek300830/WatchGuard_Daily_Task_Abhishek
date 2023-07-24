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
        # raise NotImplementedError("We can't add cars Now.")
    
ford = Garage()
# ford.add_cars("fiesta") 
# we can do instead 

car = Car("Ford", "Fiesta")
ford.add_cars(car)

print(len(ford))