# Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:

# abc
# def
# ghi

# and so on.
import string

file_path = "Practice-100-Python-Questions\Section-2\create_by_44.txt"

with open (file_path,'a') as file:
    flag = 1
    for letter in string.ascii_lowercase:
        if flag == 1:
            file.write(letter)
            flag = 2
        elif flag == 2:
            file.write(letter)
            flag = 3
        elif flag == 3:
            file.write(letter+"\n")
            flag = 1
