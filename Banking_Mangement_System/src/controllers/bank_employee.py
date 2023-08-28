from src.controllers.user import User
from src.models.database import search_in_account_withdrawn_requests, update_amount_in_account, \
    search_in_user_account_by_id, update_pending_amount_in_account, update_in_account_withdrawn_requests


class BankEmployee(User):

    def approve_withdraw_changes_by_cashier(self):
        pass

    def check_for_withdraw_requests(self):
        all_requests = search_in_account_withdrawn_requests()
        if all_requests:
            for request in all_requests:
                request_id = request[0]
                user_id = request[1]
                amount = request[3]
                done_by = request[5]
                print(f"Withdraw Requests of {amount} on (Date and Time : {request[4]} requested by {request[5]}")
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
            print("No pending Requests...")

    @staticmethod
    def __approve_withdrawn_request(user_id, amount, done_by, request_id):
        user_account_details = search_in_user_account_by_id(user_id)
        account_number = user_account_details[1]
        current_balance = user_account_details[3]
        pending_amount = user_account_details[4]
        pending_amount = str(int(pending_amount) + int(amount))

        update_amount_in_account(amount, account_number, current_balance, "Debit", done_by)
        update_pending_amount_in_account(user_id, pending_amount)
        comments = input("Enter any Comment : ")

        update_in_account_withdrawn_requests("Approved", "Manager", comments, request_id)

    @staticmethod
    def __reject_withdrawn_request(user_id, amount, request_id):
        user_account_details = search_in_user_account_by_id(user_id)
        pending_amount = user_account_details[4]
        pending_amount = str(int(pending_amount) + int(amount))
        update_pending_amount_in_account(user_id, pending_amount)

        comments = input("Enter any Comment : ")
        update_in_account_withdrawn_requests("Rejected", "Manager", comments, request_id)
