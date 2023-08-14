# Create a script that generates a text file with all letters of the English alphabet inside it, 
# one letter per line.

import string

file_path = "Practice-100-Python-Questions\Section-2\create_by_41.txt"

with open(file_path,'a') as file:
    for letter in string.ascii_lowercase:
        file.write(letter+"\n")
