# generate a list of elements from 1 to 20

list_numbers = []

for number in range(1, 21):
    list_numbers.append(number)

print(list_numbers)

# we can also do this in way like

my_range = range(1, 21)
print(list(my_range))
