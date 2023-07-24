def power_of_two():
    user_input = input("Enter Number : ")
    try:
        number = float(user_input)
    except ValueError:
        print("Please Enter Correct Value.")
        return 0.0
    else:
        number_square = number ** 2
        return number_square

print(power_of_two())
