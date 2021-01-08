# Basic intro to web scraping with Python and BeautifulSoup

This is a very basic intro to web scraping, created for a colleague to get going with scraping news sites
for press releases. We won't be using a virtual environment or any complex, refactored code in this exercise - 
just the bare minimum to get going. 



## Getting started

I'm using a MacBook Pro 2014 with Visual Code Studio editor and iTerm terminal as my command line. Any code editor will do, as well as terminal. If you are on Windows, I can try and find the set-up for that, but I have almost zero experience coding on a Windows PC.

Linux should be similar to the Mac set-up, but I'm guessing if you're using Linux you won't need my help much here.

I'm using Python 3, rather than the almost deprecated Python 2. I still have to type: $python3 app.py as typing 'python' will still use Python 2. 

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