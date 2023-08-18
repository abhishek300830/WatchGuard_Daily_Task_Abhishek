# Please take a look at the following list:

checklist = ["Portugal", "Germany", "Munster", "Spain"]

# One of the items is not a country. Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

all_countries_file_path = "Practice-100-Python-Questions\Section-4\countries_clean_86.txt"

with open(all_countries_file_path,'r') as file:
    all_countries_list = file.readlines()
    all_countries_list = [x.strip("\n") for x in all_countries_list]
    
    valid_checklist = [x for x in checklist if x in all_countries_list]

print(valid_checklist)