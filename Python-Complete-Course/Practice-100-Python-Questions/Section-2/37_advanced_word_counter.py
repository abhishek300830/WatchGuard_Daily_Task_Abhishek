#  Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
file_path = "Practice-100-Python-Questions\Section-2\words2.txt"
with open(file_path,'r') as file:
    file_data = file.read().replace(","," ")
    len_file_data = len(file_data.split(" "))
    print(len_file_data)