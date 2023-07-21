# without inheritance code will look like
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary
    
    def average(self):
        return sum(self.marks) / len(self.marks)

student_one = WorkingStudent("Kunal","CU",30000)
print(student_one.salary)

## but with inheritance 

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
# inheriting student class
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    def weekly_salary(self):
        return self.salary / 4
    

student_one = WorkingStudent("Kunal","CU",30000)
student_one.marks.append(86)
student_one.marks.append(50)
student_one.marks.append(90)

avg = student_one.average()
print(avg)
print(student_one.weekly_salary())

