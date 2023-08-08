def user_has_permission(func):
    def secure_func(*args, **awargs):
        return func(*args, **awargs)
    return secure_func

@user_has_permission
def my_function(param):
    return f"this is my fuction {param}"

@user_has_permission
def another_function():
    return f"this is function without arguments"
    

print(my_function("abhishek"))
print(another_function())



