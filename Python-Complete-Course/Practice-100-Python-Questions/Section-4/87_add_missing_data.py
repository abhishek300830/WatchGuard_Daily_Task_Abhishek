checklist = ['Portugal', 'Germany', 'Spain']

missing_countries_file_path = "Practice-100-Python-Questions\Section-4\countries_missing_87.txt"
all_countries_file_path = "Practice-100-Python-Questions\Section-4\countries_all_87.txt"


with open(missing_countries_file_path,'r') as file:
    missing_countries_list = file.readlines()

    missing_countries_list = [x.strip("\n") for x in missing_countries_list]
    
    all_countries_list = missing_countries_list+checklist
    all_countries_list.sort()

with open(all_countries_file_path,'w') as file:
    for country in all_countries_list:
        file.write(country+'\n')
