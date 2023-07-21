# without classes
my_student = {
    "name":"Abhishek",
    "grades":[80,90,100]
}

def average(student):
    return sum(student['grades'])/ len(student['grades'])

print(average(my_student))

''' 
with classes
self is the blank object and we are creating name and grade 
iside it 
'''
class Student:
    def __init__(self,new_name,new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades)/len(self.grades)

# we can create object of Student class like that
student_one = Student("Abhishek",[80,95,82])
Abhishek_average = student_one.average()

print(Abhishek_average)

#we can call in different way like
# these two are doing same thing
Student.average(student_one)
student_one.average()