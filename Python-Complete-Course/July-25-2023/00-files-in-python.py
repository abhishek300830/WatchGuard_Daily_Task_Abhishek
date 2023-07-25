# "r" is used for reading the file
my_file = open('Python-Complete-Course\July-25-2023\data.txt','r')
file_content = my_file.read()

my_file.close()
# make sure that files are opened for smallest possible time

print(file_content)

# lets write something to file
# "w" will override the existing file

user_entered_text = input("Enter anything you want to write : ")
my_file_writing = open('Python-Complete-Course\July-25-2023\data.txt','w')
my_file_writing.write(user_entered_text)

my_file_writing.close()

