import json

json_file = open("Python-Complete-Course\July-25-2023\\friends_json.json",'r')

file_content = json.load(json_file) # reads file and turns it into dictionary
json_file.close()

# print(file_content["friends"][0]['name'])

# converting python structure to JSON using dumps
cars = [
    {'make':'ford','model':'fiesta'},
    {'make':'ford','model':'focus'}
]

cars_file = open("Python-Complete-Course\July-25-2023\cars_json.json",'w')

json.dump(cars,cars_file)
cars_file.close()

# we can use Loads and while working on string.

my_json_string = '[{"name":"Abhishek","degree":"Btech"}]'

python_list  = json.loads(my_json_string)
print(python_list[0]['name'])