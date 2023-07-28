friends = {"aryan","abhishek",'kunal'}

friend_name = input("Enter friend Name : ")
friend_name_set ={friend_name,}

friends_nearby = friend_name_set.intersection(friends)

if any(friends_nearby):
    print("nearby Friend found")
else:
    print("Friend not found")