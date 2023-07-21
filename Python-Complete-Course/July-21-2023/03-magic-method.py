# magic methods in python
class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]
    
    def __repr__(self):
        return f"<Garage {self.cars}>"

    def __str__(self):
        return f"Garage with {len(self.cars)} cars"
    
ford = Garage()
ford.cars.append("fiesta")
ford.cars.append("focus")

# this is only give length if we have already defined __len__
print(ford)
print(len(ford))

print(ford[0])   #same as Garage.__getItem__(self,index)

for car in ford:
    print(car)