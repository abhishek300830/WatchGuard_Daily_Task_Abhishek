# Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

english_word = input("Enter Word : ")
if english_word in d:
    print(d[english_word])
else:
    print("Not Translated")