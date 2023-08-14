# Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.
file_path = "Practice-100-Python-Questions\Section-2\words1.txt"

with open(file_path,'r') as file:
    file_data = file.read()
    len_of_file_data = len(file_data.split(" "))
    print(len_of_file_data)