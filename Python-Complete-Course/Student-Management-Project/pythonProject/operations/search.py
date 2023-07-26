from utils.database import search_from_json


class Search:

    @staticmethod
    def search_student():
        name = input("Enter Student Name you are Looking for : ")
        student_found = search_from_json(name)

        if student_found == True:
            print(f"{name} found in the List")
        else:
            print("Student not Found in the List.")

