# Complete the script so that it produces the expected output. Please use my_range  as input data.

list_numbers = []

for number in range(1, 21):
    list_numbers.append(number * 10)

print(list_numbers)

# we can also do this by list comprehension

my_range = range(1, 21)

range_list_numbers = [num * 10 for num in list(my_range)]

print(range_list_numbers)
