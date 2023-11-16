from src.helpers.runtime_queries import QUERIES
from src.models.database import get_item, insert_item, get_items, update_item


class Account:
    """This class represents a user account and gives access to account methods"""

    account_number = any
    account_type = any
    account_balance = any
    pending_balance = any

    def deposit_amount(self, amount, done_by):
        """deposit_amount to customer account

        Args:
            amount (int): amount to deposit
            done_by (int): done by manager or Cashier
        """
        operation = "Credit"
        final_balance = str(self.account_balance + float(amount))
        update_item(
            QUERIES.get("UPDATE_AMOUNT_IN_ACCOUNT"),
            (final_balance, self.account_number),
        )
        update_item(
            QUERIES.get("UPDATE_TRANSACTION_OF_ACCOUNT"),
            (self.account_number, operation, amount, done_by),
        )

    def withdraw_amount(self, amount, done_by):
        """withdraw_amount from customer account

        Args:
            amount (int): amount to withdraw
            done_by (int): done by manager or Cashier
        """
        operation = "Debit"
        final_balance = str(self.account_balance - float(amount))

        if done_by == "Manager":
            update_item(
                QUERIES.get("UPDATE_AMOUNT_IN_ACCOUNT"),
                (final_balance, self.account_number),
            )
            update_item(
                QUERIES.get("UPDATE_TRANSACTION_OF_ACCOUNT"),
                (self.account_number, operation, amount, done_by),
            )

        else:
            if float(amount) >= 10000:
                user_id = self.__get_user_id_from_account()
                insert_item(
                    QUERIES.get("INSERT_INTO_ACCOUNT_WITHDRAWN_REQUESTS"),
                    (user_id, amount, done_by),
                )
                pending_amount = str(float(self.pending_balance) - float(amount))
                update_item(
                    QUERIES.get("UPDATE_PENDING_AMOUNT_IN_ACCOUNT"),
                    (pending_amount, user_id),
                )
            else:
                update_item(
                    QUERIES.get("UPDATE_AMOUNT_IN_ACCOUNT"),
                    (final_balance, self.account_number),
                )
                update_item(
                    QUERIES.get("UPDATE_TRANSACTION_OF_ACCOUNT"),
                    (self.account_number, operation, amount, done_by),
                )

    def view_balance(self, user_id):
        """view customer account balance

        Args:
            user_id (int): user id of Customer

        Returns:
            dict: user account balance
        """
        user_account_details = get_item(
            QUERIES.get("SEARCH_IN_USER_ACCOUNT_BY_ID"), (user_id,)
        )

        return user_account_details

    def __get_user_id_from_account(self):
        """get user id from account Number

        Returns:
            int: user id of Account Holder
        """
        account_details = get_item(
            QUERIES.get("SEARCH_IN_USER_ACCOUNT"), (self.account_number,)
        )
        user_id = account_details[0]
        return user_id

    def set_customer_account_details(self, user_id):
        """used to set customer account details in variables for futher operations

        Args:
            user_id (int): user id of current logged in user
        """
        user_account_details = get_item(
            QUERIES.get("SEARCH_IN_USER_ACCOUNT_BY_ID"), (user_id,)
        )
        self.account_number = user_account_details[1]
        self.account_type = user_account_details[2]
        self.account_balance = user_account_details[3]
        self.pending_balance = user_account_details[4]

    def print_passbook(self, user_id):
        """get all Account Transaction of Customer Account

        Args:
            user_id (int): user id of current logged in user

        Returns:
            dict: Account Transaction details of Customer Account
        """
        self.set_customer_account_details(user_id)
        account_transactions = get_items(
            QUERIES.get("SEARCH_IN_ACCOUNT_TRANSACTIONS"), (self.account_number,)
        )
        return account_transactions

    def verify_account(self, user_account):
        """verify account number is present in database

        Args:
            user_account (int): Account number of Customer

        Returns:
            dict: account details if account is present in database
        """
        self.account_number = user_account
        account_details = get_item(
            QUERIES.get("SEARCH_IN_USER_ACCOUNT"), (user_account,)
        )

        if account_details is not None:
            self.account_number = account_details[1]
            self.account_type = account_details[2]
            self.account_balance = account_details[3]
            self.pending_balance = account_details[4]
        return account_details
