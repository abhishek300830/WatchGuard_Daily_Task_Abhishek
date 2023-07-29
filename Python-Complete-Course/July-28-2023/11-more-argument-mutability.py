
age = 20

def increase_age(current_age):
    current_age = current_age + 1

print(id(age))
increase_age(age)
print(id(age))
age = age + 1
print(id(age))

# it gives same id because age is 20 anyway
# current age is increased which is a another memory location
# because int is immuatable

# let see this with a list
print("working with primes")

primes = [2,3,5]

print(id(primes))
primes += [7,11]  # primes = primes.__iadd__()  same memory location
print(id(primes))
primes = primes + [13,17] # prime = prime.__add__() new memory location

# the value is same because inner value is changing now outer