# method Overloading
class Human:
    def say_hello(self, name = None):
        if name is not None:
            print(f"Hello {name}")
        else:
            print("Hello! ")


abhishek = Human()

abhishek.say_hello()
abhishek.say_hello("Abhishek")