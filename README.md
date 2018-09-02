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
>Beautiful Soup,scrappy is used for Static Scraping

#### Dynamic Scraping
Dynamic scraping uses an actual browser and lets JavaScript do its thing. Then, it queries the **Document Object Model**(DOM) to extract the content it's looking for. Sometimes we need to automate the browser by simulating a user to get the content you need.
>Selenium is used for Dynamic Scraping

## Requesting with UserAgent
```       
                import random  
                headers={'User-Agent':user_agents[random.randint(0,8)]} 
                r= requests.get(pageUrl, headers=headers)  
                html= r.text.encode("utf8")  
                soup = BeautifulSoup( html,'lxml')  

```
>You can also specify header as  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

# For More Information
Learn more about the Beautiful soup at the page of [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)




