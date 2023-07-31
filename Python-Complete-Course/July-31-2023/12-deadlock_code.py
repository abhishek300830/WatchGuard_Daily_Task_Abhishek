from threading import Thread,Lock

account_one = Lock()
account_two = Lock()

def transfer(account_one,account_two):
    account_one.acquire()
    account_two.acquire()
    print("Transaction Done")
    account_two.release()
    account_two.release()