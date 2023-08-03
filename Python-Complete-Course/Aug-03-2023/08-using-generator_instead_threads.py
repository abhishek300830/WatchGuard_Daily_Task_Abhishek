def countdown(count):
    while count > 0:
        yield count
        count -= 1


c1 = countdown(10)
c2 = countdown(20)

print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))