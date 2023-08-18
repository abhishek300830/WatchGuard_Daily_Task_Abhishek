# Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries

countries_area_file_path = "Practice-100-Python-Questions\Section-4\countries_by_area_88.txt"

# list_according_to_desity = []
# with open(countries_area_file_path,'r') as file:
#     file_data = file.readlines()
#     for country in file_data:
#         country_list = country.split(',') 
#         country_list = [x.strip('\t').strip('\n') for x in country_list]


import pandas
data = pandas.read_csv(countries_area_file_path)
data['density'] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index,row in data[:5].iterrows():
    print(row['country'])

# We're using pandas to load the data as a dataframe and then calculate a density column in line 4. Then we use sort_values  to sort the data by density in descending order. Lastly, in the last two lines, we access the first 5 rows of the dataframe and iterate using iterrows .