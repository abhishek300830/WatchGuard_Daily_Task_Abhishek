
def greet():
    print("Hello")

def before_and_after(func):
    print("Before...")
    func()
    print("after...")

before_and_after(greet)

movies =  [
    {"name":"The Matrix","director":"Wachowski"},
    {"name":"1917","director":"Mendus"},
    {"name":"Klaus","director":"Pablos"},
]

def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by = input("What Property are we searching for : ")
looking_for = input("What are you looking For : ")

movie = find_movie(looking_for, lambda movie:movie[find_by])

print(movie or "No Movie Find")


