from collections import deque
friends = deque(('abhi','kunal','kush','aryan'))

def get_friend():
    yield from friends

def greet(g):
    while True:
        try:
            friend = next(g)
            yield f"Hello {friend}"
        except StopIteration:
            print("Stopped")


friend_generator = get_friend()
g = greet(friend_generator)

print(next(g))
print(next(g))
print(next(g))