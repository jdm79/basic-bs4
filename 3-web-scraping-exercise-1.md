
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
$python app-1.py
```
[Previous page](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md) [Next page](https://github.com/jdm79/basic-bs4/blob/main/4-web-scraping-using-inspect.md)