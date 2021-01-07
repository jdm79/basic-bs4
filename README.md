# Basic intro to web scraping with Python and BeautifulSoup

Install a code editor (preferably Visual Code) 

Install [Visual Code here](https://code.visualstudio.com/)


## Terminal commands

Now open your terminal (I use iTerm with zshrc) and type the following commands below:

Create a folder called pr-scrapes
```
$mkdir pr-scrapes
```

Go into that folder
```
$cd pr-scrapes
```

Create a python file called app.py
```
$touch app.py
```

Open everything in this folder on the code editor
```
$code .
```

## On Visual Code Editor 

Click on app.py file and copy and paste in the code which is in this app.py on my repository.


Install the two libraries we will be using on your terminal (you can use the terminal on Visual Code by pressing ~ and ctrl at the same time):

Requests will make the HTTP request to the website we want to scrape
```
$pip install requests
```

BeautifulSoup parses the returned HTML and allows us to play with the text (string)
```
$pip install beautifulsoup4
```

now you have everything ready to make a scrape

to run the code in your terminal:

```
$python app.py
```

The scraped HTML page will be returned in your terminal. Have a look at the div tags and see where the information you want to scrape is. These are the tags we will target in the next little scrape.

One of the best ways to identify where to target HTML tags (on Chrome anyway) is to right-click inspect and browse the 'elements' section and hover over, click and search through the different tags to see where the information you want is. When you hover over the different divs in 'elements' you will see on the left on the website itself what you are hovering over.