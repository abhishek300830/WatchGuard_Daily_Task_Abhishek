#  Create a program that, once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.
import time
time_counter = 1

while True:
    print("Hello ",time_counter)
    time.sleep(time_counter)
    time_counter = time_counter + 1

