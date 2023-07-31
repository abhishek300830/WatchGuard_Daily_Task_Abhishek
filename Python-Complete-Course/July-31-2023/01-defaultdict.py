from collections import defaultdict


user_list =[('name','abhi'),('id','123')]


dictionary = defaultdict(list)

for user in user_list:
    dictionary[user[0]].append(user[1])


print(dictionary['name'])
print(dictionary["key"])

# another example to understand this

# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])

# 1
# 2
# Not Present