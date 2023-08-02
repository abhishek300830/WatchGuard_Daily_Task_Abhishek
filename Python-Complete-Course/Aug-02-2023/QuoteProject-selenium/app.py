import requests
from selenium import webdriver
from pages.quotes_page import QuotePage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from : ")
    tag = input("Enter your Tag : ")

    chrome = webdriver.Chrome()
    chrome.get("https://quotes.toscrape.com/search.aspx")
    page = QuotePage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred.")

