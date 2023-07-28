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