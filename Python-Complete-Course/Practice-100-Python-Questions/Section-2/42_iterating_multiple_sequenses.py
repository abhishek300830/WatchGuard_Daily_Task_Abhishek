#  Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

zipped = zip(a,b)
print(type(zipped))
print(dict(zipped))

for x in range(0,3):
    print(a[x]+b[x])