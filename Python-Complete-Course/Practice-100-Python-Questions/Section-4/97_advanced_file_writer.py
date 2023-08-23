# create a program that asks the user to submit text repeatedly
# the program save the changes when user enter SAVE but doesn't close.
#  the program closes with user submit CLOSE

file_path = r"Practice-100-Python-Questions\Section-4\user_data_commas_95.txt"

line_list = []

while True:
    line = input("Enter a Value(CLOSE for exit, SAVE for saving) : ")
    if line == "CLOSE":
        break
    elif line == "SAVE":
        with open(file_path,"a+") as file:
            for line in line_list:
                file.write(line+'\n')
        line_list = []
    else:
        line_list.append(line)