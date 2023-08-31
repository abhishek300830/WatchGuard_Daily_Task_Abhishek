from src.controllers.user import User
from src.models.database import get_item, insert_item, \
    update_item
from src.utils import queries
from tabulate import tabulate


class Customer(User):

    def register_new_customer(self, user_id, user_role):
        if user_role == "Manager":
            verified = 1
        else:
            verified = 0
        customer_details = (
            user_id, self.name, self.email, self.phone_no, self.id_proof_type, self.id_proof, self.gender, verified)
        insert_item(queries.INSERT_INTO_USERS_TABLE, customer_details)
        print("********************************")
        self.create_customer_account(user_id)

        if user_role == "Manager":
            print("Account Created Successfully.")
        else:
            print("Account Approval Request send to Manager")

    def create_customer_account(self, user_id):
        account_number = str(int(user_id) * 1000)
        account_type = 'Saving'
        account_balance = 2500
        pending_balance = 0
        account_details = (user_id, account_number, account_type, account_balance, pending_balance)
        insert_item(queries.INSERT_INTO_ACCOUNT_TABLE, account_details)

    def edit_customer_details(self, user_id, attribute_to_update, attribute_value, role):
        if role == 'Manager':
            update_item(queries.UPDATE_USERS_BY_ID.format(attribute_to_update), (attribute_value, user_id))
        else:
            insert_item(queries.INSERT_INTO_USER_DETAIL_MODIFICATION,
                        (user_id, attribute_to_update, attribute_value, "Pending"))

    def view_customer_details(self, user_id):
        user_details = get_item(queries.SEARCH_USER_BY_ID, (user_id,))

        user_details_list = [
            ["Name", user_details[1]],
            ["Email", user_details[2]],
            ["Phone", user_details[3]],
            ["ID Type", user_details[4]],
            ["ID Number", user_details[5]],
            ["Gender", user_details[6]]
        ]

        print("***** Customer Details *****")
        print(tabulate(user_details_list, tablefmt="grid"))
