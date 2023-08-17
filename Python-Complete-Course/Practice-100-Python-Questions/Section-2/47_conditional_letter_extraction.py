import glob

file_list = glob.glob("Practice-100-Python-Questions\Section-2\\files_generated\*.txt")
match_string = "python"
final_list = []

for file_path in file_list:
    with open(file_path,'r') as file:
        letter = file.read().strip("\n")
        if letter in match_string:
            final_list.append(letter)

print(final_list)
