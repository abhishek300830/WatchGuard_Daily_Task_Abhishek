# Create a function that takes any string as input 
# and returns the number of words for that string.

def string_splitter(string : str):
    res = string.split(" ")
    return(len(res))

print(string_splitter("my name is ..."))

