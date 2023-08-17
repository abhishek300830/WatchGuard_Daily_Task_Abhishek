# read from json add employee and save to json

import json
from pprint import pprint

file_path = "Practice-100-Python-Questions\Section-3\json_data_58.json"

with open(file_path,"r+") as file:
    dictionary = json.loads(file.read())
    dictionary["employees"].append({"firstName":"Abhishek","lastName":"Kumar"})
    file.seek(0)
    json.dump(dictionary,file,indent=4,sort_keys=True)
    file.truncate()
    

