
ages = [22, 21, 25, 19, 18, 20]

# here we add condition after the for loop 
odd_ages = [age for age in ages if age % 2 == 1]
print(odd_ages)

# if condtion are complex it is better to use normal implementation
# for better understanding.

# 
friends =  ["Abhi","Aryan",'John']
guests = ["Abhi",'john',"kush"]

friends_lower = [friend.lower() for friend in friends]

present_friends = [
    name.title()
      for name in guests
        if name.lower() in friends_lower 
]
print(present_friends)