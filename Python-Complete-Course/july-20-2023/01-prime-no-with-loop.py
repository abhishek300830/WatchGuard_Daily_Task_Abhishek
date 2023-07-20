
for number in range (2,10):
    for i in range(2,number):
        if number % i == 0:
            print(f"Number equal to {i} * {number//i}")
            break
    else:
        print("This is prime Number.")
    
