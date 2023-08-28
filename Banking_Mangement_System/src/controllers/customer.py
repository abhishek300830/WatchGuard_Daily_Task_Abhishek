from src.controllers.user import User
from src.models.database import get_item, insert_item, \
    update_item
from src.utils import queries


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
        print("Customer Registered Successfully.")
        self.create_customer_account(user_id)
        print("Account Created Successfully.")

    @staticmethod
    def create_customer_account(user_id):
        account_number = str(int(user_id) * 1000)
        account_type = 'Saving'
        account_balance = 2500
        pending_balance = 0
        account_details = (user_id, account_number, account_type, account_balance, pending_balance)
        insert_item(queries.INSERT_INTO_ACCOUNT_TABLE, account_details)

    @staticmethod
    def edit_customer_details(user_id, attribute_to_update, attribute_value, role):
        if role == 'Manager':
            update_item(queries.UPDATE_USERS_BY_ID.format(attribute_to_update), (attribute_value, user_id))
        else:
            insert_item(queries.INSERT_INTO_USER_DETAIL_MODIFICATION,
                        (user_id, attribute_to_update, attribute_value, "Pending"))

    @staticmethod
    def view_customer_details(user_id):
        user_details = get_item(queries.SEARCH_USER_BY_ID, (user_id,))
        print("*******************************************")
        print("Customer Name : ", user_details[1])
        print("Customer Email : ", user_details[2])
        print("Customer Phone : ", user_details[3])
        print("Customer ID Type : ", user_details[4])
        print("Customer ID Number : ", user_details[5])
        print("Customer Gender : ", user_details[6])
        print("*******************************************")
