# to use regex we import
import re

email = "abhishek@gmail.com"

expression = "[a-z\.]+"

matches= re.findall(expression,email)

print(type(matches))
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)

# we can also do this type of thing like
email = "aryan@gmail.com"
parts = email.split('@')
print(parts)