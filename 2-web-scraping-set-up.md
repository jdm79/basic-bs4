## Index
  1. [Intro](https://github.com/jdm79/basic-bs4/blob/main/1-web-scraping-intro.md)
  2. [Setting up and installing the tools](https://github.com/jdm79/basic-bs4/blob/main/2-web-scraping-set-up.md)
  3. [The webs scraping exercise](https://github.com/jdm79/basic-bs4/blob/main/3-web-scraping-exercise-1.md)
  4. [Using inspect with Chrome](https://github.com/jdm79/basic-bs4/blob/main/4-web-scraping-using-inspect.md)

# Set-up

Before we start any coding, we need to make sure we have all the correct tools. Setting up anything in coding is often half the battle.

First we need to install a code editor (preferably Visual Code). If you already have one and use it, etc: great. If not: install [Visual Code here](https://code.visualstudio.com/)

To open your terminal, press CMD and spacebar together and type 'terminal', then open it up.

On your terminal type (but don't type the dollar sign - type everything after the $):

```
$python --version
```
![alt text](https://github.com/jdm79/basic-bs4/blob/main/img/python-version.png?raw=true)


If it is something like 2.7.16, type the following on your terminal:
```
$python3 --version
```
I'm on 3.9.0 but anything with over 3 is good for this. Because Python 2 is still around on some machines, you might have to type python3 rather than python in order to run files. This will use Python 3 to run/install things. In newer Macs this might not be an issue, but the best way to check is by trying both.

If nothing comes up when you check python3 version, you will need to download python3 [here](https://www.python.org/downloads/). Once downloaded and set up, check the version as shown above before moving on.

The next thing we will need is [pip](https://pip.pypa.io/en/stable/). This is the Python package manager which we use to install packages/libraries we want to use in projects. Libraries are pre-written code by expert geeks which will do a lot of the heavy lifting for us, meaning we only need to import the library and read the documentation to see what their methods do. Check if you have pip already by typing the following in your terminal:
```
$pip --version
```
![alt text](https://github.com/jdm79/basic-bs4/blob/main/img/pip-version.png?raw=true)


If this doesn't work, try:
```
$pip3 --version
```

I have version 20.3.3. As long as it's around that, it's fine. If you have a Mac, it should have come with Python. If you do not have pip, you will need to install it by typing the following into your terminal (using Homebrew):
```
$brew install pip3
```


[Previous page](https://github.com/jdm79/basic-bs4/blob/main/1-web-scraping-intro.md)   [Next page](https://github.com/jdm79/basic-bs4/blob/main/3-web-scraping-exercise-1.md)