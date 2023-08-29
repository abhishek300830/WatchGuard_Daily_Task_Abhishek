from src.models.database import get_item, \
    insert_item, get_items, update_item
from src.utils import queries


class Account:
    account_number = any
    account_type = any
    account_balance = any
    pending_balance = any

    def deposit_amount(self, amount, done_by):
        operation = 'Credit'
        final_balance = str(self.account_balance + float(amount))
        update_item(queries.UPDATE_AMOUNT_IN_ACCOUNT, (final_balance, self.account_number))
        update_item(queries.UPDATE_TRANSACTION_OF_ACCOUNT, (self.account_number, operation, amount, done_by))

    def withdraw_amount(self, amount, done_by):
        operation = 'Debit'
        final_balance = str(self.account_balance - float(amount))

        if done_by == "Manager":
            update_item(queries.UPDATE_AMOUNT_IN_ACCOUNT, (final_balance, self.account_number))
            update_item(queries.UPDATE_TRANSACTION_OF_ACCOUNT, (self.account_number, operation, amount, done_by))

        else:
            if float(amount) >= 10000:
                user_id = self.__get_user_id_from_account()
                insert_item(queries.INSERT_INTO_ACCOUNT_WITHDRAWN_REQUESTS, (user_id, amount, done_by))
                pending_amount = str(float(self.pending_balance) - float(amount))
                update_item(queries.UPDATE_PENDING_AMOUNT_IN_ACCOUNT, (pending_amount, user_id))
            else:
                update_item(queries.UPDATE_AMOUNT_IN_ACCOUNT, (final_balance, self.account_number))
                update_item(queries.UPDATE_TRANSACTION_OF_ACCOUNT, (self.account_number, operation, amount, done_by))


    def view_balance(self, user_id):
        user_account_details = get_item(queries.SEARCH_IN_USER_ACCOUNT_BY_ID, (user_id,))
        return user_account_details

    def __get_user_id_from_account(self):
        account_details = get_item(queries.SEARCH_IN_USER_ACCOUNT, (self.account_number,))
        user_id = account_details[0]
        return user_id

    def set_customer_account_details(self, user_id):
        user_account_details = get_item(queries.SEARCH_IN_USER_ACCOUNT_BY_ID, (user_id,))
        self.account_number = user_account_details[1]
        self.account_type = user_account_details[2]
        self.account_balance = user_account_details[3]
        self.pending_balance = user_account_details[4]

    def print_passbook(self, user_id):
        self.set_customer_account_details(user_id)
        account_transactions = get_items(queries.SEARCH_IN_ACCOUNT_TRANSACTIONS, (self.account_number,))
        return account_transactions

    def verify_account(self, user_account):
        self.account_number = user_account
        account_details = get_item(queries.SEARCH_IN_USER_ACCOUNT, (user_account,))

        if account_details is not None:
            self.account_number = account_details[1]
            self.account_type = account_details[2]
            self.account_balance = account_details[3]
            self.pending_balance = account_details[4]
        return account_details


