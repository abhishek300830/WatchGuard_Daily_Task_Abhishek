from itertools import product,permutations,combinations

list1 = [1,2,3]
list2 = [2,34,45]

result = product(list1,list2)
print(list(result))

print(list(product(range(1,7),repeat=2)))

p_1 = permutations("ABC")
P_limited =permutations("ABC",r=2)

print(list(p_1))
print(list(P_limited))

c_1 = combinations("ABC", r=2)
print(list(c_1))