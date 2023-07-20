# without enumerate function

friends = ["abhi","kunal","kush"]
counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter += 1

# with enumerate function

for index, friend in enumerate(friends):
    print(index)
    print(friend)


# we can also use it with list

enumerated_list = list(enumerate(friends))
enumerated_dict = dict(enumerate(friends))
print(enumerated_list)  # list of tuples
print(enumerated_dict)  
   
