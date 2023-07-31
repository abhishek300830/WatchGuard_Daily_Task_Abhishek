from collections import deque

friends =  deque(("Abhi","Aryan","Kunal","kush"))

friends.append("chirag")
friends.appendleft("Abhay")

print(friends)

friends.popleft()
friends.pop()

print(friends)