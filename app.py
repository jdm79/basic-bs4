#!/usr/bin/env python3

from bs4 import BeautifulSoup # this is the library that deals with the returned HTML. An HTTP parser
import requests # this is the library for making HTTP requests
from requests import get # 'get' is the common web name for making an HTTP request

# an HTTP request is when you send a request to the url address to grab some kind of info from it
# in this first example, we're just grabbing the whole HTML of the page
# a POST request sends info/data to a website/server while GET just asks for info/data from a website/server


url = "https://www.interpol.int/News-and-Events" # setting the variable 'url' with the value of interpol's news 
page = requests.get(url) # this goes to the interpol website and saves the response as a value to variable 'page'
soup = BeautifulSoup(page.content, 'html.parser') # Beautiful Soup takes the HTML and extracts the data

print(soup)
