import mysql.connector

from src.models.context_manager import DBConnection


def search_by_username(username):
    with DBConnection() as cursor:
        try:
            cursor.execute("SELECT * FROM authentication WHERE username = %s", (username,))
            user_auth = cursor.fetchone()
        except mysql.connector.Error as error:
            print(error)

        return user_auth


def search_users_by_id(user_id):
    with DBConnection() as cursor:
        try:
            cursor.execute("SELECT * FROM users Where id = %s", (user_id,))
            user_details = cursor.fetchone()
        except mysql.connector.Error as error:
            print(error)

        return user_details


def insert_into_auth_table(username, password, role):
    with DBConnection() as cursor:
        try:
            cursor.execute("INSERT INTO authentication (username,password,role,created_at) values (%s,%s,%s,"
                           "current_timestamp())", (username, password, role))
        except mysql.connector.Error as error:
            print(error)


def insert_into_users_table(customer_details):
    with DBConnection() as cursor:
        try:
            cursor.execute("insert into users values (%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(),current_timestamp())",
                           customer_details)
        except mysql.connector.Error as error:
            print(error)


def insert_into_account_table(account_details):
    with DBConnection() as cursor:
        try:
            cursor.execute("insert into user_account (id,account_number,account_type,account_balance,pending_balance,"
                           "created_at) values (%s,%s,%s,%s,%s,current_timestamp())", account_details)
        except mysql.connector.Error as error:
            print(error)


def search_in_user_account(user_account):
    with DBConnection() as cursor:
        try:
            cursor.execute("select * from user_account where account_number = %s", (user_account,))
            account_details = cursor.fetchone()
        except mysql.connector.Error as error:
            print(error)

        return account_details


def update_amount_in_account(amount, account, current_balance, operation, done_by):
    current_balance = float(current_balance)
    if operation == 'Credit':
        final_balance = str(current_balance + float(amount))
    else:
        final_balance = str(current_balance - float(amount))
    with DBConnection() as cursor:
        try:
            cursor.execute("UPDATE user_account SET account_balance = %s WHERE account_number = %s",
                           (final_balance, account))
            cursor.execute("INSERT into account_transactions (account_number,transaction_type,amount,created_at,"
                           "done_by)"
                           "values (%s,%s,%s,current_timestamp(),%s)", (account, operation, amount, done_by))
        except mysql.connector.Error as error:
            print(error)


def update_pending_amount_in_account(user_id, pending_amount):
    with DBConnection() as cursor:
        try:
            cursor.execute("UPDATE user_account SET pending_balance = %s WHERE id = %s", (pending_amount, user_id))
        except mysql.connector.Error as error:
            print(error)


def update_users_by_id(user_id, attribute_to_update, attribute_value):
    with DBConnection() as cursor:
        try:
            cursor.execute(f"update users set {attribute_to_update} = %s where id = %s", (attribute_value, user_id))
        except mysql.connector.Error as error:
            print(error)


def insert_into_user_detail_modification(user_id, attribute_to_update, attribute_value, status):
    with DBConnection() as cursor:
        try:
            cursor.execute("insert into user_details_modification (uid,attribute_to_update,attribute_value,status) "
                           "values"
                           "(%s,%s,%s,%s)", (user_id, attribute_to_update, attribute_value, status))
        except mysql.connector.Error as error:
            print(error)


def update_password_in_auth(username, password):
    with DBConnection() as cursor:
        try:
            cursor.execute("update authentication set password = %s where username = %s", (password, username))
        except mysql.connector.Error as error:
            print(error)


def search_in_user_account_by_id(user_id):
    with DBConnection() as cursor:
        try:
            cursor.execute("select * from user_account where id = %s", (user_id,))
            user_account_details = cursor.fetchone()
        except mysql.connector.Error as error:
            print(error)

        return user_account_details


def search_in_account_transactions(account_number):
    with DBConnection() as cursor:
        try:
            cursor.execute("select * from account_transactions where account_number = %s", (account_number,))
            account_transactions = cursor.fetchall()
        except mysql.connector.Error as error:
            print(error)

        return account_transactions


def insert_into_account_withdraw_requests(uid, amount, requested_by):
    with DBConnection() as cursor:
        try:
            cursor.execute("insert into account_withdraw_requests (uid,status,debited_amount,date,requested_by) "
                           "values ("
                           "%s,'Pending',%s,current_timestamp(),%s)", (uid, amount, requested_by))
        except mysql.connector.Error as error:
            print(error)


def search_in_account_withdrawn_requests():
    with DBConnection() as cursor:
        try:
            cursor.execute("select * from account_withdraw_requests where status = 'Pending'")
            all_requests = cursor.fetchall()
        except mysql.connector.Error as error:
            print(error)
        return all_requests


def update_in_account_withdrawn_requests(status, approved_by, comments, request_id):
    with DBConnection() as cursor:
        try:
            cursor.execute(
                "update account_withdraw_requests set status = %s,approved_by = %s,comments = %s where id = %s",
                (status, approved_by, comments, request_id))
        except mysql.connector.Error as error:
            print(error)
