# Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

import time

timecounter = 0

while True:
    print("Hello ",timecounter)
    timecounter = timecounter + 1

    if timecounter > 3:
        print("End of Loop")
        break
    
    time.sleep(timecounter)