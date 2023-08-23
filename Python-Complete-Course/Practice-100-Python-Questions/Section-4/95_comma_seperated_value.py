line = input("Enter Lines : ")
line_list = line.split(",")

file_path = r"Practice-100-Python-Questions\Section-4\user_data_commas_95.txt"

with open(file_path,"a+") as file:
    for i in line_list:
        file.write(i+'\n')
