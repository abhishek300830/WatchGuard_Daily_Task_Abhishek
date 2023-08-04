from collections import deque
from types import coroutine

friends = deque(('Abhi','Kunal',"Kush","Chirag"))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

async def greet(friend):
    print("Starting....")
    await friend
    print("Ending...")

friend = friend_upper()
print("friend ",friend)

g = greet(friend)
print("g ",g)

g.send(None)
g.send("Hello")
g.send("Good")



