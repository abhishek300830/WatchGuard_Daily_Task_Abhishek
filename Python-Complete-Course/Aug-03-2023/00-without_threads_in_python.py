import time

def ask_user():
    start  = time.time()
    user_input = input("Enter your Name : ")
    greet = f"Hello ,{user_input}"
    print(greet)
    print("ask user time",time.time()-start)

def complex_Calculation():
    start  = time.time()
    print("starting calculation.")
    [x**2 for x in range(80000000)]
    print("Calculation completed")
    print("complex calculation",time.time()-start)


start = time.time()
ask_user()
complex_Calculation()
print("Single thread time ",time.time()-start)

