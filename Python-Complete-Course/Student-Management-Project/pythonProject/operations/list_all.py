from utils.database import get_data_from_json


class List_all:
    @staticmethod
    def list_all_students():
        student_data = get_data_from_json()
        for student in student_data:
            print(student)

