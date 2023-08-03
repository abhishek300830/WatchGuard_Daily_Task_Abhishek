from collections import deque

friends = deque(("Abhi","kunal","kush",'aryan'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("HELLO")
print("hello .....")
greeter.send("GOOD")