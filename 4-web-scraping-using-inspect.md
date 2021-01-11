## Index
  1. [Intro](https://github.com/jdm79/basic-bs4/blob/main/1-web-scraping-intro.md)
  2. [Setting up and installing the tools](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md)
  3. [The webs scraping exercise](https://github.com/jdm79/basic-bs4/blob/main/3-web-scraping-exercise-1.md)
  4. [Using inspect with Chrome](https://github.com/jdm79/basic-bs4/blob/main/4-web-scraping-using-inspect.md)

# How to find what you want from an HTML page

One of the best ways to identify where to target HTML tags (on Chrome anyway) is to right-click inspect
and browse the 'elements' section and hover over, click and search through the different tags to see where
the information you want is. 

![alt text](https://github.com/jdm79/basic-bs4/blob/main/img/inspect-2.png?raw=true)



When you hover over the different divs in 'elements' you will see on the left on the website itself 
what you are hovering over. Below we can see that the text we want is in an <a> tag with the class name 'gem-c-document-list__item-title'. That is the information BeautifulSoup needs to grab the part of the HTML we want. We use the method .find_all because there are more than one tags. If it was just one tag to find, like the main title, we would use .find. 

![alt text](https://github.com/jdm79/basic-bs4/blob/main/img/inspect-3.png?raw=true)



Here we target the exact part of the HTML we want to grab. This can take a bit of trial and error. Sometimes divs are nested inside more divs, until it's hard to see where anything really is. Sometimes it's not so bad.

You can even change and extend this code, to use a different URL and scrape from a different website. You will have to see where 


[Previous page](https://github.com/jdm79/basic-bs4/blob/main/3-web-scraping-exercise-1.md)