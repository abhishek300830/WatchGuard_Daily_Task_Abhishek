# Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

print(d)

# d1 = {a for a in d.items() if a[1]<=1}

d2 = dict((key,value) for key,value in d.items() if value<=1)
print(d2)

