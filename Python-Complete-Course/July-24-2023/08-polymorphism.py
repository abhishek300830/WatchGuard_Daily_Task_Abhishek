class Bird:
    def flight(self):
        print("bird can fly")

class Sparrow(Bird):
    def flight(self):
        print("sparrow can fly")

bird = Bird()
bird.flight()

sparrow = Sparrow()
sparrow.flight()