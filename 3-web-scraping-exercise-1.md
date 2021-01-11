
# Setting up the folder and files for this project

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

now you have everything ready to make a scrape

to run the code in your terminal:

```
$python app-1.py
```


[Previous page](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md) [Next page](https://github.com/jdm79/basic-bs4/blob/main/4-web-scraping-using-inspect.md)