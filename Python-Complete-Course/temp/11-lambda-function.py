# normal function
def divide(x, y):
    return x/y

# identical lambda function

divide = lambda x, y: x / y
print(divide(10,3))

# we can also call it like but this is not a clean code
print((lambda x, y: x / y)(10,3))

# lamda function at a time provide simplicity to code however
# at a time they can also make it complicated.