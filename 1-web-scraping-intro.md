# Basic intro to web scraping for journalists

The example I'll use for this tutorial is the UK government Office of National Statistics () website, which publishes data and articles about pretty much everything. For this exercise we want to write a Python script that visits the main [research and statistics page](https://www.gov.uk/search/research-and-statistics). This is a constantly updated list of articles and datasets. Publications, institutes, academics and private companies jump on these as soon as they come out, to make data graphics, find stories, obtain specific data etc. Whatever. 

For this exercise we just want to grab the titles of the latest published stats. This could be handy if you had a specific interest in something that is often published on ONS: you could add to your script a checker which alerts you if it's something you want - or have some code that downloads the stats file automatically to a database or perhaps emails it to you.

Or in this case, it gives you a list of the latest titles which you can look at in your terminal.



Here we target the exact part of the HTML we want to grab. This can take a bit of trial and error. I didn’t quite drill down to the exact div, but was able to clean up what I did grab and work with that. Go over all the issues on the HTML page and put them into an array to use later.

Loop over the array, sort the issues alphabetically and create a string which separates each issue with a comma and space.


[Next page](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md)