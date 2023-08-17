while True:
    psw = input("Enter your New Password : ")

    is_valid_length = False
    is_uppercase = False
    is_number = False

    if any(i.isdigit() for i in psw):
        is_number = True
    else:
        print("Please include Number.")
    if any(i.isupper() for i in psw):
        is_uppercase = True
    else:
        print("Please Include Upper Case Letter.")
    if len(psw) >= 5:
        is_valid_length = True
    else:
        print("Password length is less than 5")
    
    if is_valid_length and is_uppercase and is_number:
        print("Good Password")
        break
    else:
        print("Try Again...")
        
    