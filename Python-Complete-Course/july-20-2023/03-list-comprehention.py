numbers = [0, 1, 2, 3, 4]

doubled_number = []

for number in numbers:
    doubled_number.append(number * 2)

print(doubled_number)

# we can also do this by using list comprehention like

doubled_number = [number * 2 for number in numbers]
print(doubled_number)

# applying with string
friends_age = [22, 31, 25, 21]

age_strings = [f"you are {age} year old." for age in friends_age]
print(age_strings)

# making all names in list lowercase
friends_name = ["ABHI","RAHUL"]

friends_name_lower = [name.lower() for name in friends_name]
print(friends_name_lower)