# by default
class Student:
    def say_hello(cls): 
        print(cls) 

student_one = Student()
student_one.say_hello() # here student_one is passed

# classmethod
class Student:
    @classmethod
    def say_hello(cls):
        print(cls.__name__) # Student

student_one = Student()
student_one.say_hello() # here student is passed 

# static method
class Student:
    @staticmethod
    def say_hello():
        print("static don't take arguments")

student_one = Student()
student_one.say_hello() 