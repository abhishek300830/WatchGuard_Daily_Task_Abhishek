# write a script that extracts letter from the 26 files and put the letters in the list
import string

file_path = "Practice-100-Python-Questions\Section-2\\files_generated"

letter_list = []

for letter in string.ascii_lowercase:
    with open(f"{file_path}\{letter}.txt",'r') as file:
        letter_list.append(file.read())

print(letter_list)

#  another way of doing it
letter_list_2 = []
import glob
file_list = glob.glob("Practice-100-Python-Questions\Section-2\\files_generated\*.txt")

for file_name in file_list:
    with open(file_name,'r') as file:
        letter_list_2.append(file.read().strip("\n"))
        
print(letter_list_2)
print(letter_list_2)
