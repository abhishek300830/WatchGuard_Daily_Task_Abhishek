import functools

users = {'username':'abhishek','access_level':'admin'}
def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(panel):
            '''
            Hey i will be called secretly...
            '''
            if users.get("access_level")==access_level:
                return func(panel)
        return secure_func
    return user_has_permission
        
@third_level('admin')
def my_function(panel):
    print(f'password for {panel} panel is 1234')


my_function('movies')
print(my_function.__name__)
print(my_function.__doc__)