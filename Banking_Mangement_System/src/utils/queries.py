# SEARCH QUERIES
SEARCH_USER_BY_USERNAME = "SELECT * FROM authentication WHERE username = %s"

SEARCH_USER_BY_ID = "SELECT * FROM users Where id = %s"

SEARCH_IN_USER_ACCOUNT = "select * from user_account where account_number = %s"

SEARCH_IN_ACCOUNT_WITHDRAWN_REQUESTS = "select * from account_withdraw_requests where status = %s"

SEARCH_IN_ACCOUNT_TRANSACTIONS = "select * from account_transactions where account_number = %s"

SEARCH_IN_USER_ACCOUNT_BY_ID = "select * from user_account where id = %s"

SEARCH_USERS_BY_ACCOUNT_STATUS = "SELECT * FROM users Where verified = %s"

SEARCH_PENDING_REQ_IN_DETAIL_MODIFICATION = "SELECT * FROM user_details_modification where status = %s"

#  INSERT QUERIES
INSERT_INTO_AUTH_TABLE = ("INSERT INTO authentication (username,password,role,created_at) values (%s,%s,%s,"
                          "current_timestamp())")

INSERT_INTO_USERS_TABLE = "insert into users values (%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(),current_timestamp())"

INSERT_INTO_ACCOUNT_TABLE = ("insert into user_account (id,account_number,account_type,account_balance,"
                             "pending_balance,created_at) values (%s,%s,%s,%s,%s,current_timestamp())")

INSERT_INTO_USER_DETAIL_MODIFICATION = ("insert into user_details_modification (uid,attribute_to_update,"
                                        "attribute_value,status) values (%s,%s,%s,%s)")

INSERT_INTO_ACCOUNT_WITHDRAWN_REQUESTS = ("insert into account_withdraw_requests (uid,status,debited_amount,date,"
                                          "requested_by) values (%s,'Pending',%s,current_timestamp(),%s)")

# UPDATE QUERIES
UPDATE_USERS_BY_ID = "update users set {} = %s where id = %s"

UPDATE_PASSWORD_IN_AUTH = "update authentication set password = %s where username = %s"

UPDATE_IN_ACCOUNT_WITHDRAWN_REQUESTS = ("update account_withdraw_requests set status = %s,approved_by = %s,comments = "
                                        "%s where id = %s")

UPDATE_PENDING_AMOUNT_IN_ACCOUNT = "UPDATE user_account SET pending_balance = %s WHERE id = %s"

UPDATE_AMOUNT_IN_ACCOUNT = "UPDATE user_account SET account_balance = %s WHERE account_number = %s"

UPDATE_TRANSACTION_OF_ACCOUNT = ("INSERT into account_transactions (account_number,transaction_type,amount,created_at,"
                                 "done_by) values (%s,%s,%s,current_timestamp(),%s)")

UPDATE_VERIFIED_STATUS_OF_CUSTOMER = "update users set verified = 1 where id = %s"

UPDATE_USER_DETAIL_MODIFICATION_STATUS = "update user_details_modification set status = %s where id = %s"
