from bs4 import BeautifulSoup # this is the library that deals with the returned HTML. An HTTP parser
import requests # this is the library for making HTTP requests
from requests import get # 'get' is the common web name for making an HTTP request

# an HTTP request is when you send a request to the url address to grab some kind of info from it
# in this first example, we're just grabbing the whole HTML of the page
# a POST request sends info/data to a website/server while GET just asks for info/data from a website/server

# setting the variable 'url' with the value of the gov.uk website URL 
url = "https://www.gov.uk/search/research-and-statistics?content_store_document_type=published_statistics" 
headers = {"Accept-language": "en-US, en;q=0.5"}

page = requests.get(url, headers=headers) # this goes to the gov.uk website and saves the response as a value to variable 'page'
# soup = BeautifulSoup(page.content, 'html.parser') # Beautiful Soup takes the HTML and extracts the data
soup = BeautifulSoup(page.text, "html.parser")

# this will print the entire HTML of the web page we just contacted in the command line terminal
print(soup)
