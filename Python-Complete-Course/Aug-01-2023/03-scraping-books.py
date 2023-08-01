import requests
from bs4 import BeautifulSoup

# website_content = requests.get('https://books.toscrape.com/')
page = requests.get('https://www.example.com/')

print(type(page))
print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])

