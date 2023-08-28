from src.models.database import search_in_user_account, update_amount_in_account, search_in_user_account_by_id, \
    search_in_account_transactions, insert_into_account_withdraw_requests, update_pending_amount_in_account


class Account:
    account_number = any
    account_type = any
    account_balance = any
    pending_balance = any

    def deposit_amount(self, amount, done_by):
        operation = 'Credit'
        update_amount_in_account(amount, self.account_number, self.account_balance, operation, done_by)

    def withdraw_amount(self, amount, done_by):
        operation = 'Debit'
        if done_by == "Manager":
            update_amount_in_account(amount, self.account_number, self.account_balance, operation, done_by)
        else:
            if float(amount) >= 10000:
                user_id = self.get_user_id_from_account()
                insert_into_account_withdraw_requests(user_id, amount, done_by)
                pending_amount = str(float(self.pending_balance) - float(amount))
                update_pending_amount_in_account(user_id, pending_amount)
            else:
                update_amount_in_account(amount, self.account_number, self.account_balance, operation, done_by)

    @staticmethod
    def view_balance(user_id):
        user_account_details = search_in_user_account_by_id(user_id)
        return user_account_details

    def get_user_id_from_account(self):
        account_details = search_in_user_account(self.account_number)
        user_id = account_details[0]
        return user_id

    def set_customer_account_details(self, user_id):
        user_account_details = search_in_user_account_by_id(user_id)
        self.account_number = user_account_details[1]
        self.account_type = user_account_details[2]
        self.account_balance = user_account_details[3]
        self.pending_balance = user_account_details[4]

    def print_passbook(self, user_id):
        self.set_customer_account_details(user_id)
        account_transactions = search_in_account_transactions(self.account_number)
        return account_transactions

    def verify_account(self, user_account):
        self.account_number = user_account
        account_details = search_in_user_account(user_account)
        if account_details is not None:
            self.account_number = account_details[1]
            self.account_type = account_details[2]
            self.account_balance = account_details[3]
            self.pending_balance = account_details[4]
        return account_details
