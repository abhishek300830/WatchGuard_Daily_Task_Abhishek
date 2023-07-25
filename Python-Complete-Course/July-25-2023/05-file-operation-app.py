import sys
sys.path.append('Python-Complete-Course\July-25-2023')

import file_operations

file_path = "Python-Complete-Course\July-25-2023\\file-operation.txt"

file_operations.save_to_file("Abhishek save this data",file_path)
readed_file = file_operations.read_file("Python-Complete-Course\July-25-2023\\file-operation.txt")
print(readed_file)