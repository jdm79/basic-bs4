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

# this new variable will contain all the titles of new articles on the ONS site page
# .find_all is a BeautifulSoup method which will find every <a> tag with a class of'gem-c-document-list__item-title'
# and grab the data from inside it. We're getting closer to what we want.
# This will still be HTML though
results_html = soup.find_all('a', class_='gem-c-document-list__item-title')
# print(results_html)

# this creates an empty Python list, which we will fill below with titles
title_list = []

# this is a basic 'for loop' which will iterate over the results_list created above,
# and for each item in this object it will create a container. 
# in each container we will ask for only the text from the container and call that variable 'title'.
# .append is a Python list method which adds title to the list
# .strip is a BeautifulSoup method which strips away all the white space, otherwise it would look mental
for container in results_html:
    title = container.text
    title_list.append(title.strip())

# now we have to create another 'for loop' to iterate over each item in the list and print that item
for title in title_list:
    print(title)