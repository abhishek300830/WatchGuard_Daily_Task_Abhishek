# Store the dictionary in a json file.
import json

filepath ="Practice-100-Python-Questions\Section-3\json_data_56.json"
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}


with open(filepath,'w') as file:
    json.dump(d,file,indent=4)

# he argument indent=4  will create 4 white spaces to indent the different levels of the dictionary items.