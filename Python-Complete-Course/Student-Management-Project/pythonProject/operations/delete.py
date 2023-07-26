from utils import database


class Delete:
    @staticmethod
    def delete_student():
        name = input("Enter Name of student you want to delete: ")
        database.delete_from_json(name)
        print("Student Deleted Successfully.")
