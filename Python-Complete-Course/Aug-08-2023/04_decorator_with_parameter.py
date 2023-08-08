import functools

users = {'username':'abhishek','access_level':'admin'}

def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        '''
        Hey i will be called secretly...
        '''
        if users.get("access_level")=='admin':
            return func(panel)
    return secure_func
        
@user_has_permission
def my_function(panel):
    print(f'password for {panel} panel is 1234')


my_function('movies')
print(my_function.__name__)
print(my_function.__doc__)