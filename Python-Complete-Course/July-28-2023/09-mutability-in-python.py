"""
integer -> all functions return new int object
float 
string
tuple
"""

friend_last_seen = {
    'Rolf' : 31,
    'Jen': 1,
    'Ane': 7,
}

print(id(friend_last_seen))

another_variable = friend_last_seen
print(id(friend_last_seen))
print(id(another_variable))


friend_last_seen = {
    'Rolf' : 31,
    'Jen': 1,
    'Ane': 7,
}
print(id(friend_last_seen))
friend_last_seen['Rolf'] = 0

# so dictionary are mutable we can change their value but memory location is same

print(id(friend_last_seen))

print("working with int")
my_int = 5

print(id(my_int))

my_int =my_int+1

# here int can't modify itself it return new object so id are different

print(id(my_int))

print("working with list")

friends = ['abhi', 'kunal']
print(id(friends))

friends.append('kush')
print(id(friends))