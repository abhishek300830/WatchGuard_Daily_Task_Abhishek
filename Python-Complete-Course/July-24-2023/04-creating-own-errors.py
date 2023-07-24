class MyCustomError(TypeError):
    '''Exception occur when called
    '''
    def __init__(self , message , code):
        super().__init__(f"Error Code {code}: {message}")
        self.code = code

# raise MyCustomError("An Error Happened",500)
err =  MyCustomError("An Error Happened",500)
err_doc = err.__doc__
print(err)
print(err_doc)