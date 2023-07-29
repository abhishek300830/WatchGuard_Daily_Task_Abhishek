class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
users = [
    {
        "username":'abhi',
        "password":'123'
    },
    {
        "username":'kunal',
        "password":'1234'
    }
]


user_objects = [User(username=data['username'],password=data['password']) for data in users]

for user in user_objects:
    print(user.username)

# we can do it with argument unpacking in way like

user_objects = [User(**data) for data in users]

for user in user_objects:
    print(user.username)



d = {'k1':10, 'k2':20, 'k3':30}
def fun(k1,k2,k3):
    print(k1,k2,k3)
fun(*d) 
fun(**d) 

# k1 k2 k3
# 10 20 30