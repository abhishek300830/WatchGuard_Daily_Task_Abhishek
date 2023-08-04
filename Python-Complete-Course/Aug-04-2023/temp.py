from threading import Thread
import threading
import sys
import time
def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
    
sys.setswitchinterval(50)
start = time.time()
fib(36)
fib(36)
fib(36)
print(time.time()-start, "Time Taken.")
threading.Timer()

t1 = Thread(target=fib,args=(36,))
t2 = Thread(target=fib,args=(36,))
t3 = Thread(target=fib,args=(36,))
start = time.time()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(time.time()-start, "Time Taken.")


