# WebScrap in Python
This repo contains the various methods to extract data out of webpages (web scraping) using a python script 

# Different Packages
* Beautiful Soup
* Selenium
* Scrappy


###### Beautiful Soup
>BeautifulSoup is used for extracting data points from the pages that are loaded. Beautiful Soup is quite robust and it handles nicely malformed markup.Beautiful Soup creates a **parse tree** that can be used to extract data from HTML.

###### Selenium
>Selenium is first of all a **tool writing automated tests for web applications**. It’s used for web scraping mainly because it’s beginner-friendly and if a site uses JavaScript


# Beautiful Soup VS Selenium

#### Static Scraping
Static scraping ignores JavaScript. It fetches web pages from the server without the help of a browser.We can get exactly what we see in "view page source", and then manipulate with that
>**Beautiful Soup,scrappy is used for Static Scraping**

#### Dynamic Scraping
Dynamic scraping uses an actual browser and lets JavaScript do its thing. Then, it queries the **Document Object Model**(DOM) to extract the content it's looking for. Sometimes we need to automate the browser by simulating a user to get the content you need.
>**Selenium is used for Dynamic Scraping**

## UserAgent
```       
Web browser will send what is known as a “User Agent” for every page you access. This is a string to tell the server what kind of device we are accessing the page with.

Some webpages will use the User Agent to display content that is customized to your particular browser. For example if your User Agent indicates you are using an old browser then the website may return the plain HTML version without any AJAX features, which may be easier to scrape.Some websites will automatically block certain User Agents
```

>You can find your own current **User Agent** [here](http://httpbin.org/get)

# Lets Get Started!!!




