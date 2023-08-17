#  create a script that search the term in the google

import webbrowser

query = input("What you want to search : ")
webbrowser.open(f"https://www.google.com/search?q={query}")

# We're using webbrowser  here which is a standard library that is used to open a web browser.

# First, we're getting the search term stored in variable query via the input  function. You need to first do a manual search on Google and observe how Google will construct the URL. Depending on where you are in the world the URL may be different, but the above URL should work everywhere.