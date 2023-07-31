import time

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)

def power(limit):
    return [x**2 for x in range(limit)]

# measure_runtime(lambda: power(50000000))

# theres is a in built function which made it easy 
import timeit


print(timeit.timeit("[x**2 for x in range(500)]"))