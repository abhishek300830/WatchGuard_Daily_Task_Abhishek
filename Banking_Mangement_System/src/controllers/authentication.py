import hashlib

from src.models.database import get_item, insert_item, update_item
from src.utils import queries


class Authentication:
    username = any
    password = any
    role = any

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self):
        valid_user = get_item(queries.SEARCH_USER_BY_USERNAME, (self.username,))

        if valid_user is None:
            print("Please Enter Valid Username...")
        else:
            hashed_password = self.__hashing_password()
            valid_password = valid_user[2]

            if hashed_password == valid_password:
                print("login Successfully")
                print("*******************************")
                self.__assigning_role(valid_user[3])
                return valid_user
            else:
                print("Please Enter Correct Password...")
                return None

    def change_password(self, username, old_password, new_password):
        self.password = old_password
        hashed_password = self.__hashing_password()

        valid_user_details = get_item(queries.SEARCH_USER_BY_USERNAME, (username,))

        if valid_user_details is None:
            print("Please Enter Valid Username...")
        else:
            valid_password = valid_user_details[2]

            if valid_password == hashed_password:
                self.password = new_password
                hashed_new_password = self.__hashing_password()
                update_item(queries.UPDATE_PASSWORD_IN_AUTH, (hashed_new_password, username))
                print("Password Updated Successfully")
            else:
                print("Your Old Password is Wrong...")

    def __hashing_password(self):
        encoded_password = self.password.encode()
        hashed_password = hashlib.sha256(encoded_password).hexdigest()
        return hashed_password

    def __assigning_role(self, user_role):
        self.role = user_role

    def create_customer_auth_account(self):
        hashed_password = self.__hashing_password()
        insert_item(queries.INSERT_INTO_AUTH_TABLE, (self.username, hashed_password, "Customer"))
        user_auth = get_item(queries.SEARCH_USER_BY_USERNAME, (self.username,))
        return user_auth[0]
