import time
from multiprocessing import Process

def ask_user():
    start  = time.time()
    user_input = input("Enter your Name : ")
    greet = f"Hello ,{user_input}"
    print(greet)
    print("ask user time",time.time()-start)

def complex_Calculation():
    start  = time.time()
    print("starting calculation.")
    [x**2 for x in range(40000000)]
    print("Calculation completed")
    print("complex calculation",time.time()-start)


# processes 
process1 = Process(target=complex_Calculation)
process2 = Process(target=complex_Calculation)
process1.start()
process2.start()

start = time.time()

process1.join()
process2.join()


print(f"Two Process total time : {time.time()-start}")