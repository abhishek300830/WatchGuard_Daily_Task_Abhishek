class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    # added decorator
    @property
    def average(self):
        return sum(self.marks) / len(self.marks)

student_one = Student("abhishek","CU")
student_one.marks.append(89)
student_one.marks.append(92)

print(student_one.average)