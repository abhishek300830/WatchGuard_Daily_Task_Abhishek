import hashlib

from src.models.database import search_by_username, insert_into_auth_table, update_password_in_auth


class Authentication:
    username = any
    password = any
    role = any

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self):
        valid_user = search_by_username(self.username)
        if valid_user is None:
            print("Please Enter Valid Username...")
        else:
            hashed_password = self.hashing_password()
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
        hashed_password = self.hashing_password()

        valid_user_details = search_by_username(username)
        if valid_user_details is None:
            print("Please Enter Valid Username...")
        else:
            valid_password = valid_user_details[2]
            if valid_password == hashed_password:
                self.password = new_password
                hashed_new_password = self.hashing_password()
                update_password_in_auth(username, hashed_new_password)
                print("Password Updated Successfully")
            else:
                print("Your Old Password is Wrong...")

    def hashing_password(self):
        encoded_password = self.password.encode()
        hashed_password = hashlib.sha256(encoded_password).hexdigest()
        return hashed_password

    def __assigning_role(self, user_role):
        self.role = user_role

    def create_customer_auth_account(self):
        hashed_password = self.hashing_password()
        insert_into_auth_table(self.username, hashed_password, "Customer")
        user_auth = search_by_username(self.username)
        return user_auth[0]
