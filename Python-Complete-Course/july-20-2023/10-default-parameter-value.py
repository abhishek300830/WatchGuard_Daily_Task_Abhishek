# here if num2 is not passed by default taken to be 30
def add(num1,num2 = 30):
    total = num1 + num2
    return total

added_value =  add(10)
added_value =  add(num1=10) # we can also do this
# if one argument have name like num1, all variable passing must 
# have names

print(added_value)

# we can also use seperater while printing value

print(1, 2, 3, 4, 5, sep="-")