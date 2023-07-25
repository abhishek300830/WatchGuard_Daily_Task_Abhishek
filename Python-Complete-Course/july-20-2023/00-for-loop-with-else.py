cars_status = ["ok","ok","ok","faulty","ok"]

for status in cars_status:
    if status == "faulty":
        print("stopping the production")
        break
    print(f"The car is {status}")

# if we remove fauly from cars_status else block will execute 
else:
    print("Finally! All cars build successfully.")