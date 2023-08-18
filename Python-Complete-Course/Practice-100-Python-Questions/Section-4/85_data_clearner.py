#  Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 

# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.

countries_raw_file_path = "Practice-100-Python-Questions\Section-4\countries_raw_85.txt"
countries_new_file_path = "Practice-100-Python-Questions\Section-4\countries_new_85.txt"


with open(countries_raw_file_path,"r") as file:
    countries_raw_list = file.readlines()
    countries_new_list = [x.strip('\n') for x in countries_raw_list if len(x) > 2]

with open(countries_new_file_path,'a') as file:
    for country in countries_new_list:
        file.write(country+"\n")