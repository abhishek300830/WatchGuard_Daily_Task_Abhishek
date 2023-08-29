from src.controllers.user import User
from src.helpers.validators import validate_name
from src.models.database import get_items, update_item, get_item
from src.utils import queries


class BankEmployee(User):

    def check_for_withdraw_requests(self):
        all_requests = get_items(queries.SEARCH_IN_ACCOUNT_WITHDRAWN_REQUESTS, ("Pending",))
        if all_requests:
            for request in all_requests:
                request_id = request[0]
                user_id = request[1]
                amount = request[3]
                done_by = request[5]
                print(f"Withdraw Requests of {amount} on (Date and Time : {request[4]} ) requested by {request[5]}.")
                while True:
                    manager_choice = input("1. Approve\n2. Reject \n Enter (1,2) : ")
                    if manager_choice == '1':
                        self.__approve_withdrawn_request(user_id, amount, done_by, request_id)
                        break
                    if manager_choice == '2':
                        self.__reject_withdrawn_request(user_id, amount, request_id)
                        break
                    else:
                        print("Please Enter Valid Input...")
        else:
            print("No pending Withdrawn Requests.")

    def __approve_withdrawn_request(self, user_id, amount, done_by, request_id):
        user_account_details = get_item(queries.SEARCH_IN_USER_ACCOUNT_BY_ID, (user_id,))
        account_number = user_account_details[1]
        current_balance = user_account_details[3]
        pending_amount = user_account_details[4]
        pending_amount = str(int(pending_amount) + int(amount))
        final_balance = str(current_balance - float(amount))

        update_item(queries.UPDATE_AMOUNT_IN_ACCOUNT, (final_balance, account_number))
        update_item(queries.UPDATE_TRANSACTION_OF_ACCOUNT, (account_number, "Debit", amount, done_by))
        update_item(queries.UPDATE_PENDING_AMOUNT_IN_ACCOUNT, (pending_amount, user_id))

        self.__input_comment()

        update_item(queries.UPDATE_IN_ACCOUNT_WITHDRAWN_REQUESTS, ("Approved", "Manager", self.comment, request_id))


    def __reject_withdrawn_request(self, user_id, amount, request_id):
        user_account_details = get_item(queries.SEARCH_IN_USER_ACCOUNT_BY_ID, (user_id,))
        pending_amount = user_account_details[4]
        pending_amount = str(int(pending_amount) + int(amount))
        update_item(queries.UPDATE_PENDING_AMOUNT_IN_ACCOUNT, (pending_amount, user_id))

        self.__input_comment()

        update_item(queries.UPDATE_IN_ACCOUNT_WITHDRAWN_REQUESTS, ("Rejected", "Manager", self.comment, request_id))

    def __input_comment(self):
        self.comment = input("Enter any Comment : ")
        is_valid_comment = validate_name(self.comment)
        if is_valid_comment is None:
            print("Please Enter Valid Comment.")
            self.__input_comment()

    @staticmethod
    def check_for_new_registration_request():
        not_verified_user_details = get_items(queries.SEARCH_USERS_BY_ACCOUNT_STATUS, (0,))

        if not_verified_user_details:
            for user in not_verified_user_details:
                user_id = user[0]
                name = user[1]
                email = user[2]
                phone_no = user[3]
                print(f"Account Creation Request of {name}\nEmail : {email}\nPhone No : {phone_no}")

                while True:
                    manager_choice = input("1. Approve\n2. Reject \n Enter (1,2) : ")
                    if manager_choice == '1':
                        update_item(queries.UPDATE_VERIFIED_STATUS_OF_CUSTOMER, (user_id,))
                        break
                    if manager_choice == '2':
                        break
                    else:
                        print("Please Enter Valid Input...")
        else:
            print("No Pending Registration Requests.")

    @staticmethod
    def check_for_user_modification_request():
        pending_modification_requests = get_items(queries.SEARCH_PENDING_REQ_IN_DETAIL_MODIFICATION, ("Pending",))

        if pending_modification_requests:
            for request in pending_modification_requests:
                request_id = request[0]
                user_id = request[1]
                account_no = int(request[1])*1000
                attribute_to_update = request[2]
                attribute_value = request[3]
                print("************************************")
                print(f"For Account Number {account_no}\n{attribute_to_update.capitalize()} Updation Request.")
                print(f"New {attribute_to_update.capitalize()} is {attribute_value}")

                while True:
                    manager_choice = input("1. Approve\n2. Reject \n Enter (1,2) : ")
                    if manager_choice == '1':
                        update_item(queries.UPDATE_USERS_BY_ID.format(attribute_to_update), (attribute_value, user_id))
                        update_item(queries.UPDATE_USER_DETAIL_MODIFICATION_STATUS, ("Approved", request_id))
                        break
                    if manager_choice == '2':
                        update_item(queries.UPDATE_USER_DETAIL_MODIFICATION_STATUS, ("Rejected", request_id))
                        break
                    else:
                        print("Please Enter Valid Input...")

        else:
            print("No Pending User Modification Requests.")
