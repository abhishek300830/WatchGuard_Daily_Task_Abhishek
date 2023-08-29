import maskpass

from tabulate import tabulate
from src.controllers.account import Account
from src.controllers.authentication import Authentication
from src.controllers.bank_employee import BankEmployee
from src.controllers.customer import Customer
from src.helpers.validators import validate_number, validate_username, validate_password, validate_name, validate_email, \
    validate_phone
from src.utils.prompts import CUSTOMER_MENU, MANAGER_MENU, CASHIER_MENU
from src.controllers.user import User
from src.models.database import get_item
from src.utils import queries
from src.utils.prompts import LOGIN_MENU


class LoginView:

    def __init__(self):
        self.user_is_verified = None
        self.username = any
        self.password = any

    def prompt_input_username_password(self):
        self.username = input("Enter your Username : ")
        self.password = maskpass.askpass(prompt="Enter your Password : ", mask='*')

    def initializing_user(self, user_id, role):
        user_details = get_item(queries.SEARCH_USER_BY_ID, (user_id,))
        self.user_is_verified = user_details[7]

        filtered_user_details = user_details[1:7]
        current_user = User(role, *filtered_user_details)
        return current_user

    def login_view(self):
        user_choice = input(LOGIN_MENU)

        while user_choice != '2':
            if user_choice == '1':
                self.prompt_input_username_password()
                auth = Authentication(username=self.username, password=self.password)
                user_details = auth.login()

                if user_details is not None:
                    user_id = user_details[0]
                    role = user_details[3]
                    user = self.initializing_user(user_id, role)
                    EntryMenu(user, user_id, self.user_is_verified)
            else:
                print("*****************************")
                print("Invalid Input...Try Again...")
            user_choice = input(LOGIN_MENU)


class EntryMenu:

    def __init__(self, user, user_id, is_verified):
        self.user = user
        self.user_id = user_id

        if user.role == "Manager":
            self.check_for_pending_requests()
            self.manager_menu()
        elif user.role == "Cashier":
            self.cashier_menu()
        else:
            if is_verified:
                self.customer_menu()
            else:
                print("*****************************************************")
                print("Your Account is Not Verified...Contact Bank Manager.")

    def customer_menu(self):
        customer_choice = input(CUSTOMER_MENU)
        instance = Account()

        while customer_choice != '5':
            if customer_choice == '1':
                self.view_customer_balance(instance)

            elif customer_choice == '2':
                self.print_customer_passbook(instance)

            elif customer_choice == '3':
                self.transfer_to_another_account(instance)

            elif customer_choice == '4':
                self.change_user_password()

            else:
                print("****************************")
                print("Invalid Input...Try Again...")

            customer_choice = input(CUSTOMER_MENU)

    def manager_menu(self):
        manager_choice = input(MANAGER_MENU)

        while manager_choice != '7':
            if manager_choice == '1':
                self.register_new_customer()

            elif manager_choice == '2':
                self.deposit_to_customer_account()

            elif manager_choice == '3':
                self.withdraw_from_customer_account()

            elif manager_choice == '4':
                self.view_customer_details()

            elif manager_choice == '5':
                self.edit_customer_details()

            elif manager_choice == '6':
                self.change_user_password()

            else:
                print("****************************")
                print("Invalid Input...Try Again...")

            manager_choice = input(MANAGER_MENU)

    def cashier_menu(self):
        cashier_choice = input(CASHIER_MENU)

        while cashier_choice != '7':
            if cashier_choice == '1':
                self.register_new_customer()

            elif cashier_choice == '2':
                self.deposit_to_customer_account()

            elif cashier_choice == '3':
                self.withdraw_from_customer_account()

            elif cashier_choice == '4':
                self.view_customer_details()

            elif cashier_choice == '5':
                self.edit_customer_details()

            elif cashier_choice == '6':
                self.change_user_password()
            else:
                print("****************************")
                print("Invalid Input...Try Again...")

            cashier_choice = input(CASHIER_MENU)

    def input_new_customer_details(self):
        print("********************************")
        print("Customer Account Creation Portal")

        self.__input_customer_name()
        self.__input_customer_email()
        self.__input_customer_phone_no()
        self.__input_customer_id_proof_type()
        self.__input_customer_id_proof()
        self.__input_customer_gender()
        new_customer_details = (
            self.customer_name, self.customer_email, self.customer_phone_no, self.customer_id_proof_type,
            self.customer_id_proof, self.customer_gender)
        return new_customer_details

    def __input_customer_name(self):
        self.customer_name = input("Enter Customer Name : ")
        is_valid_name = validate_name(self.customer_name)
        if is_valid_name is None:
            print("Please Enter Valid Name...")
            self.__input_customer_name()

    def __input_customer_email(self):
        self.customer_email = input("Enter Customer Email: ")
        is_valid_email = validate_email(self.customer_email)
        if is_valid_email is None:
            print("Please Enter Valid Email...")
            self.__input_customer_email()

    def __input_customer_phone_no(self):
        self.customer_phone_no = input("Enter Customer Phone No: ")
        is_valid_phone = validate_phone(self.customer_phone_no)
        if is_valid_phone is None:
            print("Please Enter Valid Phone No...")
            self.__input_customer_phone_no()

    def __input_customer_id_proof_type(self):
        self.customer_id_proof_type = any
        while True:
            user_choice = input("ID Proof Type \n1. Aadhar Card\n2. Pan Card\n Please Enter your Choice(1,2....): ")
            if user_choice == '1':
                self.customer_id_proof_type = "Aadhar Card"
                break
            elif user_choice == '2':
                self.customer_id_proof_type = "Pan Card"
                break
            else:
                print("****************************")
                print("Please Enter Valid Input ...")

    def __input_customer_id_proof(self):
        self.customer_id_proof = input("Please Enter ID Proof Number: ")
        is_valid_id_proof = validate_number(self.customer_id_proof)
        if is_valid_id_proof is None:
            print("Enter Valid ID proof Number : ")
            self.__input_customer_id_proof()

    def __input_customer_gender(self):
        self.customer_gender = any
        while True:
            user_choice = input("Select Gender \n1. Male\n2. Female\n3. Other \n Please Enter your Choice(1,2....): ")
            if user_choice == '1':
                self.customer_gender = "Male"
                break
            elif user_choice == '2':
                self.customer_gender = "Female"
                break
            elif user_choice == '3':
                self.customer_gender = "Other"
                break
            else:
                print("****************************")
                print("Please Enter Valid Input ...")

    def create_customer_auth_account(self):
        self.__input_new_username()
        self.__input_new_password()

        instance = Authentication(self.new_user_name, self.new_password)
        user_id = instance.create_customer_auth_account()
        return user_id

    def __input_new_username(self):
        self.new_user_name = input("Enter Customer New Username : ")
        is_valid_username = validate_username(self.new_user_name)
        if is_valid_username is None:
            print("Enter a Valid Username...")
            self.__input_new_username()

    def change_user_password(self):
        self.__input_username()
        self.__input_old_password()
        self.__input_new_password()
        instance = Authentication()
        instance.change_password(self.user_name, self.old_password, self.new_password)

    def __input_username(self):
        self.user_name = input("Enter Username :")
        is_valid_username = validate_username(self.user_name)
        if is_valid_username is None:
            print("Enter a Valid Username...")
            self.__input_username()

    def __input_old_password(self):
        self.old_password = maskpass.askpass(prompt="Enter your Old Password : ", mask='*')
        is_valid_password = validate_password(self.old_password)
        if is_valid_password is None:
            print("Please Enter Valid Password.")
            self.__input_old_password()

    def __input_new_password(self):
        self.new_password = maskpass.askpass(prompt="Enter your New Password : ", mask='*')
        is_valid_password = validate_password(self.new_password)
        if is_valid_password is None:
            print("Please Enter Valid Password.")
            self.__input_new_password()

    def view_customer_balance(self, instance):
        user_account_details = instance.view_balance(self.user_id)
        account_number = user_account_details[1]
        account_balance = user_account_details[3]
        pending_balance = user_account_details[4]

        my_account_details = [
            ["Account Number", account_number],
            ["Account Balance", account_balance],
            ["Pending Balance", pending_balance]
        ]
        print(tabulate(my_account_details, tablefmt="grid"))

    def print_customer_passbook(self, instance):
        account_transactions = instance.print_passbook(self.user_id)
        if account_transactions:
            print("*************** Account Passbook *****************")
            print("Account Number : ", account_transactions[0][1])

            my_transactions_data = []
            headings = ["Sr No", "Transaction Type", "Amount", "Done By", "Date and Time"]

            for idx, transaction in enumerate(account_transactions):
                transaction_list = [idx + 1, transaction[2], transaction[3], transaction[5], transaction[4]]
                my_transactions_data.append(transaction_list)

            print(tabulate(my_transactions_data, headers=headings, tablefmt="grid"))

        else:
            print("*************************************")
            print("No Transactions Available to Show.")

    def transfer_to_another_account(self, instance):
        self.__input_amount_to_transfer()
        instance.set_customer_account_details(self.user_id)

        if float(self.amount_to_transfer) > float(instance.account_balance):
            print("Amount to Transfer is more than your Account Balance.")
        else:
            self.__input_account_to_transfer()
            account_details = instance.verify_account(self.account_to_transfer)
            if account_details is None:
                print("*******************************")
                print("No Account Found...Try Again...")
                print("*******************************")
            else:
                instance.deposit_amount(self.amount_to_transfer, self.user.role)
                instance.set_customer_account_details(self.user_id)
                instance.withdraw_amount(self.amount_to_transfer, self.user.role)
                print("*******************************")
                print("Amount Transferred Successfully.")
                print("*******************************")

    def __input_amount_to_transfer(self):
        self.amount_to_transfer = input("Enter Amount to Transfer : ")
        is_valid_amount = validate_number(self.amount_to_transfer)
        if is_valid_amount is None:
            print("*******************************")
            print("Please Enter Correct Amount...")
            self.__input_amount_to_transfer()

    def __input_account_to_transfer(self):
        self.account_to_transfer = input("Enter Account Number of Receiver Account : ")
        is_valid_account = validate_number(self.account_to_transfer)
        if is_valid_account is None:
            print("*************************************")
            print("Please Enter Valid Account Number...")
            self.__input_account_to_transfer()

    def register_new_customer(self):
        customer_id = self.create_customer_auth_account()
        new_customer_details = self.input_new_customer_details()
        instance = Customer("Customer", *new_customer_details)
        instance.register_new_customer(customer_id, self.user.role)

    def deposit_to_customer_account(self):
        self.__input_user_account()
        instance = Account()
        is_valid_account = instance.verify_account(self.user_account)
        if is_valid_account is None:
            print("*************************************")
            print("Account Not Found...Try Again...")
        else:
            self.__input_amount_to_deposit()
            instance.deposit_amount(self.amount_to_deposit, self.user.role)
            print("*************************************")
            print("Account Credited Successfully.")
            print("*************************************")

    def __input_user_account(self):
        self.user_account = input("Enter Account Number : ")
        is_valid_user_account = validate_number(self.user_account)
        if is_valid_user_account is None:
            print("*************************************")
            print("Enter Valid User Account.")
            self.__input_user_account()

    def __input_amount_to_deposit(self):
        self.amount_to_deposit = input("Enter Amount you want to deposit : ")
        is_valid_amount = validate_number(self.amount_to_deposit)
        if is_valid_amount is None:
            print("*************************************")
            print("Please Enter Valid Amount...")
            self.__input_amount_to_deposit()

    def withdraw_from_customer_account(self):
        self.__input_user_account()
        instance = Account()
        is_valid_account = instance.verify_account(self.user_account)
        if is_valid_account is None:
            print("*************************************")
            print("Account Not Found...Try Again...")
        else:
            self.__input_amount_to_withdraw()
            instance.withdraw_amount(self.amount_to_withdraw, self.user.role)
            if self.user.role == "Cashier" and int(self.amount_to_withdraw) >= 10000:
                print("*************************************")
                print("Withdraw Request Sent for Approval.")
                print("*************************************")
            else:
                print("*************************************")
                print("Account Debited Successfully.")
                print("*************************************")

    def __input_amount_to_withdraw(self):
        self.amount_to_withdraw = input("Enter Amount you want to deposit : ")
        is_valid_amount = validate_number(self.amount_to_withdraw)
        if is_valid_amount is None:
            print("*************************************")
            print("Please Enter Valid Amount...")
            self.__input_amount_to_withdraw()

    def view_customer_details(self):
        self.__input_user_account()
        instance = Account()
        valid_account_details = instance.verify_account(self.user_account)

        if valid_account_details is None:
            print("*************************************")
            print("Account Not Found...Try Again...")
        else:
            user_id = valid_account_details[0]
            customer = Customer()
            customer.view_customer_details(user_id)

    def edit_customer_details(self):
        self.__input_user_account()
        instance = Account()
        is_valid_account = instance.verify_account(self.user_account)
        if is_valid_account is None:
            print("*************************************")
            print("Account Not Found...Try Again...")
        else:
            user_id = is_valid_account[0]

            self.__input_attribute_to_update()

            customer = Customer()
            customer.edit_customer_details(user_id, self.attribute_to_update, self.attribute_value, self.user.role)
            if self.user.role == "Manager":
                print("*************************************")
                print("Details Modified Successfully.")
                print("*************************************")
            else:
                print("**************************************************")
                print("Modification Request Send to Manager for Approval.")
                print("***************************************************")

    def __input_attribute_to_update(self):
        self.attribute_to_update = None
        while True:
            print("Which Attribute you want to Update (Enter Choice 1,2... ) : ")
            user_choice = input("1. Name\n2. Email\n3. Phone No\n4. Gender\n")

            if user_choice == '1':
                self.attribute_to_update = "name"
                self.__input_attribute_name()
                break
            elif user_choice == '2':
                self.attribute_to_update = "email"
                self.__input_attribute_email()
                break
            elif user_choice == '3':
                self.attribute_to_update = "phone_no"
                self.__input_attribute_phone_no()
                break
            elif user_choice == '4':
                self.attribute_to_update = "gender"
                self.__input_attribute_gender()
                break
            else:
                print("*************************************")
                print("Please Enter Valid Input...")

    def __input_attribute_name(self):
        self.attribute_value = input("Enter New Name : ")
        is_valid_name = validate_name(self.attribute_value)
        if is_valid_name is None:
            print("*************************************")
            print("Invalid Name ... Enter Again...")
            self.__input_attribute_name()

    def __input_attribute_email(self):
        self.attribute_value = input("Enter New Email : ")
        is_valid_email = validate_email(self.attribute_value)
        if is_valid_email is None:
            print("*************************************")
            print("Please Enter Valid Email ID.")
            self.__input_attribute_email()

    def __input_attribute_phone_no(self):
        self.attribute_value = input("Enter New Phone Number : ")
        is_valid_number = validate_number(self.attribute_value)
        if is_valid_number is None:
            print("*************************************")
            print("Please Enter Valid Number.")
            self.__input_attribute_phone_no()

    def __input_attribute_gender(self):
        while True:
            print("Please Enter Your Choice (1,2...) ")
            user_choice = input("1. Male \n2. Female\n 3. Other\n")

            if user_choice == '1':
                self.attribute_value = "Male"
            elif user_choice == '2':
                self.attribute_value = "Female"
            elif user_choice == '3':
                self.attribute_value = "Other"
            else:
                print("*************************************")
                print("Please Enter Valid Input...")

    def check_for_pending_requests(self):

        instance = BankEmployee(self.user.role, self.user.name, self.user.email, self.user.phone_no,
                                self.user.id_proof_type, self.user.id_proof, self.user.gender)
        instance.check_for_withdraw_requests()
        instance.check_for_new_registration_request()
        instance.check_for_user_modification_request()
