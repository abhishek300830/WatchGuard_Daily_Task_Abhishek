import json

json_path = r"C:\Users\abkumar\PycharmProjects\pythonProject\utils\StudentData.json"


def add_to_json(student_data):
    json_data = get_data_from_json()
    json_data.append(student_data)

    with open(json_path, 'w') as file:
        json.dump(json_data, file)


def get_data_from_json():
    with open(json_path, 'r') as file:
        student_data = json.load(file)
        return student_data


def delete_from_json(student_name):
    student_data = get_data_from_json()
    filter_student = []
    for student in student_data:
        if student['name'] != student_name:
            filter_student.append(student)
    with open(json_path, 'w') as file:
        json.dump(filter_student, file)


def search_from_json(student_name):
    student_data = get_data_from_json()
    for student in student_data:
        if student['name'] == student_name:
            return True
    return False


def update_student_in_json(student_name, name, uid, phone, email):
    student_data = get_data_from_json()
    update_data = []
    for student in student_data:
        if student['name'] == student_name:
            new_student = {
                "name": name,
                "uid": uid,
                "phone": phone,
                "email": email
            }
            update_data.append(new_student)
        else:
            update_data.append(student)
    with open(json_path,'w') as file:
        json.dump(update_data,file)
