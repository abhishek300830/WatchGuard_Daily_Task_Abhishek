import maskpass

from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.helpers.entry_menu import EntryMenu
from src.models.database import search_users_by_id
from src.utils.prompts import LOGIN_MENU


class LoginView:

    def __init__(self):
        self.username = any
        self.password = any

    def prompt_input_username_password(self):
        self.username = input("Enter your Username : ")
        self.password = maskpass.askpass(prompt="Enter your Password : ", mask='*')

    @staticmethod
    def initializing_user(user_id, role):
        user_details = search_users_by_id(user_id)

        filtered_user_details = user_details[1:7]
        current_user = User(role, *filtered_user_details)
        return current_user

    def login_view(self):
        user_choice = input(LOGIN_MENU)

        while user_choice != '2':
            if user_choice == '1':
                self.prompt_input_username_password()
                auth = Authentication(username=self.username, password=self.password)
                user_details = auth.login()

                if user_details is not None:
                    user_id = user_details[0]
                    role = user_details[3]
                    user = self.initializing_user(user_id, role)
                    EntryMenu(user, user_id)
            else:
                print("Invalid Input...Try Again...")
            user_choice = input(LOGIN_MENU)
