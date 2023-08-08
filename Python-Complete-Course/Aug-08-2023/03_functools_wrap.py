import functools

users = {'username':'abhishek','access_level':'admin'}

def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        '''
        Hey i will be called secretly...
        '''
        if users.get("access_level")=='admin':
            return func()
    return secure_func
        
@user_has_permission
def my_function():
    print('password for admin panel is 1234')


my_function()
print(my_function.__name__)
print(my_function.__doc__)