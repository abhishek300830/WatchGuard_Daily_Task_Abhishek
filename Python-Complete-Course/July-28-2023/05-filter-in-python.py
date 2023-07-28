def start_with_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Abhi', 'Raman', 'Avi']

start_with_r_friends = filter(start_with_r, friends)

print(next(start_with_r_friends))
print(next(start_with_r_friends))
print(list(start_with_r_friends))
# list is empty because next remove element from iterator
