# need to create a near nearby-friend list

# readlines will give you a list of lines
# [line1, line2,.....]
# strip will remove leading and trailing whitespaes


friends =  input("Enter three friend name seperated by Commas(no space)  : ")
# array of friends name
friends = friends.split(',')

people = open("Python-Complete-Course\July-25-2023\people.txt",'r')
people_nearby = people.readlines()
people_nearby = [people.strip() for people in people_nearby]

# converting into set
friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = people_nearby_set.intersection(friends_set)


nearby_friends_file = open("Python-Complete-Course\July-25-2023\\nearbyfriends.txt",'w')

for friend in friends_nearby_set:
    print(f"{friend} is nearby MEET Him")
    nearby_friends_file.write(f"{friend}\n")    

nearby_friends_file.close()



