import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() # things to be printed out
counter_queue = queue.Queue() # amount by which to increase counter

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # waits until an item is available and locks the queue
        old_counter =counter
        counter = old_counter + increment
        job_queue.put((f"New Counter value {counter}",'-----------'))
        counter_queue.task_done() # this unlocks the queue now another thread get access to queue

thread = Thread(target=increment_manager,daemon=True)
thread.start()

def print_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()
    
Thread(target=print_manager,daemon=True).start()
# daemon = True run program continiously

def increment_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()
    
counter_queue.join()
job_queue.join()