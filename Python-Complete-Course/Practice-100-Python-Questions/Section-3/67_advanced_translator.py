d = dict(weather = "clima", earth = "terra", rain = "chuva") 

word = input("Enter Word : ")

try:
    translated = d[word]
    print(translated)
except KeyError:
    print("That word not exist")
