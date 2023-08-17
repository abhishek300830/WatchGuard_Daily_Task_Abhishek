#  please use file json_data_56 and write it to dictionary.

import json
from pprint import pprint

filepath ="Practice-100-Python-Questions\Section-3\json_data_56.json"

with open(filepath,"r") as file:
    json_data = json.loads(file.read())
    pprint(json_data)