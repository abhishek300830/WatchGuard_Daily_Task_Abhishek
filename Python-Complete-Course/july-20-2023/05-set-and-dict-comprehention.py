# using set and there property to find common
friends =  ["Abhi","Aryan",'John']
guests = ["Abhi",'john',"kush"]

friends_lower = {friend.lower() for friend in friends}
guests_lower = {guest.lower() for guest in guests}

common_friends_guests = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in common_friends_guests}
print(present_friends)

# dictionary comprehention

friends_name =  ["Abhi","Aryan",'John']
friends_age = [20, 21, 22]

friends_details = {
    friends_name[index]:friends_age[index]
    for index in range(len(friends_name))
}

print(friends_details)