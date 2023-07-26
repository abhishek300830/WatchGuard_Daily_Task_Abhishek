# from utils.database import add_to_json
from operations.student import Student
from utils.database import add_to_json


class Add:

    @staticmethod
    def input_user_data():
        new_student = Student()
        new_student.name = input("Enter your Name :")
        new_student.uid = input("Enter your UID : ")
        new_student.phone = int(input("Enter your Phone No: "))
        new_student.email = input("Enter your Mail ID  :")
        return new_student

    def add_student(self):
        new_student = self.input_user_data()
        student_data_to_add = {
            "name": new_student.name,
            "uid": new_student.uid,
            "phone": new_student.phone,
            "email": new_student.email
        }

        add_to_json(student_data_to_add)
