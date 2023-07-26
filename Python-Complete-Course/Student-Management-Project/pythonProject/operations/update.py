from utils.database import search_from_json, update_student_in_json


class Update:

    @staticmethod
    def update_Student():
        student_name = input("Enter the student Name you want to Update : ")
        student_found = search_from_json(student_name)

        if student_found:
            print("Enter New Details of User : ")
            name = input("Enter Name : ")
            uid = input("Enter UID : ")
            phone = int(input("Enter phone : "))
            email = input("Enter Email : ")

            update_student_in_json(student_name, name, uid, phone, email)
            print("Student Updated Successfully.")

        else:
            print("No Student Found with this Name.")



