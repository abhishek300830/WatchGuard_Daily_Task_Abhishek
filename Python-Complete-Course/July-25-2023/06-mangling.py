class Student:
    def __init__(self, name, uid):
        self.__name = name
        self.__uid = uid

stu1 = Student("Abhishek","20BCS9584")

# mangling accessing private member
print(stu1._Student__name)

print(dir(stu1))