import json

# change in syntax
with open("Python-Complete-Course\July-25-2023\\friends_json.json",'r') as json_file:
    file_content = json.load(json_file) # reads file and turns it into dictionary

print(file_content["friends"][0])
# here file will close automatically when we leave the indentation of with block.