class AnotherIterable:
    def __init__(self):
        self.cars = ['fiesta', 'focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)
