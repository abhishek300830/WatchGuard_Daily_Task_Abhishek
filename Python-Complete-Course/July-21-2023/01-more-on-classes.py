class Student:
    def __init__(self,new_name,new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self,status):
        avg = sum(self.grades)/len(self.grades)
        return f"{self.name} is {status} with Grade : {avg}"
    
student_one = Student("kunal",[80,70,90])

kunal_avg = student_one.average("happy")
print(kunal_avg)