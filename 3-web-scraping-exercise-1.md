
# Setting up the folder and files for this project

## Index
  1. [Intro](https://github.com/jdm79/basic-bs4/blob/main/1-web-scraping-intro.md)
  2. [Setting up and installing the tools](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md)
  3. [The webs scraping exercise](https://github.com/jdm79/basic-bs4/blob/main/3-web-scraping-exercise-1.md)
  4. [Using inspect with Chrome](https://github.com/jdm79/basic-bs4/blob/main/4-web-scraping-using-inspect.md)

On your terminal (I use iTerm with zshrc), type the following commands below which are in the light blue background:

In order to create a folder called pr-scrapes
```
$mkdir pr-scrapes
```

Go into that folder
```
$cd pr-scrapes
```

Create the two python files we will be using in this tutorial by typing:
```
$touch app-1.py app-2.py
```

Check that these files are created by typing in your terminal:
```
$ls
```

You should see two files in your directory.


Now open everything in this folder on the code editor
```
$code .
```

## On Visual Code Editor 

Click on [app-1.py](https://github.com/jdm79/basic-bs4/blob/main/app-1.py) file and copy and paste in the code which is in this app-1.py on my repository. Do the same for app-2.py, copy and pasting the code from [here](https://github.com/jdm79/basic-bs4/blob/main/app-2.py) into the file on your machine.


Install the two libraries we will be using on your terminal (you can also use the terminal on Visual Code by pressing ~ and ctrl at the same time):

Requests will make the HTTP request to the website we want to scrape
```
$pip install requests
```

BeautifulSoup parses the returned HTML and allows us to play with the text (string)
```
$pip install beautifulsoup4
```

now you have everything ready to make a scrape.

I've written comments in the two code files which explain what's going on at each step of the way. These are definitely worth reading to understand what everything does.

to run the code in your terminal:

```
$python app-1.py
```

You should see the entire HTML of the web page in the terminal. It's huge. It's interesting to scan over it to see how HTML is structured, but it's not exactly what we want for this tutorial. We want to get a list of all the latest article titles. To do that we need to run app-2.py. This code has targeted specific div tags in the HTML to grab what we want. We've then used BeautifulSoup and Python methods to clean up the result in order to give us a simple list.

```
$python app-2.py
```
![alt text](https://github.com/jdm79/basic-bs4/blob/main/img/list-titles.png?raw=true)


This should give us a simple list in the terminal. With this code, we've requested the HTML from the web page, turned it into something we can work with in Python, cleaned it up and printed it out. This is just a taster of what we can do with web scraping, but it's important to see how it works at a basic level before moving on to more complex scripts.


[Previous page](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md)   [Next page](https://github.com/jdm79/basic-bs4/blob/main/4-web-scraping-using-inspect.md)