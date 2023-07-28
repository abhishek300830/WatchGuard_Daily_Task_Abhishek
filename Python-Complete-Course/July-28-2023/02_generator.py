# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop  # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.start = n + 1
                return n
        raise StopIteration()


p = PrimeGenerator(100)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
