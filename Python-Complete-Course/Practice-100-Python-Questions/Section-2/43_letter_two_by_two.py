# Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

# ab
# cd
# ef

# and so on.

import string

file_path = "Practice-100-Python-Questions\Section-2\create_by_43.txt"

with open(file_path,'a') as file:
    flag = True
    for letter in string.ascii_lowercase:
        if flag:
            file.write(letter)
            flag = False
        else:
            file.write(letter+"\n")
            flag = True

