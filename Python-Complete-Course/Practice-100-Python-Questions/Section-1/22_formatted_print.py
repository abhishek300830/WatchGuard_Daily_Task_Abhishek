# create a dictionary of key a,b,c where each key has a value a list from
# 1-10,11-20,21-30 resp. and print
from pprint import pprint 

d = {
    "a" : [val for val in range(1,11)],
    "b" : [val for val in range(11,21)],
    "c" : [val for val in range(21,31)],
}

pprint(d)

