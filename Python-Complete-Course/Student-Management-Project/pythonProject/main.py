from operations.add import Add
from operations.delete import Delete
from operations.list_all import List_all
from operations.search import Search
from operations.update import Update

print("***** Student Management System *****")
MENU_PROMPT = ("1. Add Student\n2. Delete Student\n3. Update Student\n4. Search Student\n5. List All Student\n6. "
               "Exit\nEnter your Choice (1,2,...):")


def prompt_add_student():
    instance = Add()
    instance.add_student()


def prompt_delete_student():
    instance = Delete()
    instance.delete_student()


def prompt_update_student():
    instance = Update()
    instance.update_Student()


def prompt_search_student():
    instance = Search()
    instance.search_student()


def prompt_list_students():
    instance = List_all()
    instance.list_all_students()


user_selections = {
    '1': prompt_add_student,
    '2': prompt_delete_student,
    '3': prompt_update_student,
    '4': prompt_search_student,
    '5': prompt_list_students

}


def menu():
    user_choice = input(MENU_PROMPT)
    while user_choice != '6':
        if user_choice in user_selections:
            selection_function = user_selections[user_choice]
            selection_function()
        else:
            print("Invalid Entry...Try again...")

        user_choice = input(MENU_PROMPT)

    print("Thank You, Have a Nice Day")


if __name__ == '__main__':
    menu()
