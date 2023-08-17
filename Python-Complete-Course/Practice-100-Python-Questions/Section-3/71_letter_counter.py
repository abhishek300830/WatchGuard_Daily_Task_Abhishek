#  count the no of a in text

import requests

response = requests.get("https://pythonhow.com/media/data/universe.txt")

text = response.text

print(text)

#  by using for loop
counter = 0

for char in text:
    if char == 'a':
        counter = counter + 1

print(counter)
# using in build method 

count_is = text.count("a")
print("by in-build ",count_is)