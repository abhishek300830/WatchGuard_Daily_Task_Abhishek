# create a program that asks the user to submit text repeatedly
#  the program closes with user submit CLOSE

file_path = r"Practice-100-Python-Questions\Section-4\user_data_commas_95.txt"

while True:

    line = input("Enter a Value(CLOSE for exit) : ")
    if line == "CLOSE":
        break
    
    with open(file_path,"a+") as file:
            file.write(line+'\n')

