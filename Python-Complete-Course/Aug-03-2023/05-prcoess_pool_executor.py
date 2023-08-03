import time
from concurrent.futures import ProcessPoolExecutor


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

# process poll extractor
start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_Calculation)
    pool.submit(complex_Calculation)

print(f"Two process Tital time : {time.time()-start}")
