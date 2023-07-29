friends_last_seen  = {
    'rolf':31,
    'jen':1,
    'ane':2
}

def see_friend(friends , name):
    print(id(friends))
    friends[name] = 0

print(id(friends_last_seen))
print(id(friends_last_seen['rolf']))

see_friend(friends_last_seen,'rolf')

print(id(friends_last_seen['rolf']))
print(id(friends_last_seen))
