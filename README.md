install [Visual Code here](https://code.visualstudio.com/)

open terminal and type:


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

Install the two libraries we will be using:

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

the scraped HTML page will be returned in your terminal