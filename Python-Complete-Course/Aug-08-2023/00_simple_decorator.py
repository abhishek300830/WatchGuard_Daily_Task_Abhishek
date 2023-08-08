users = {'username':'abhishek','access_level':'admin'}

def user_has_permission(func):
    if users.get("access_level")=='admin':
        return func
    else:
        raise RuntimeError

def my_function():
    return 'password for admin panel is 1234'

my_secure_function = user_has_permission(my_function)
print(my_secure_function())