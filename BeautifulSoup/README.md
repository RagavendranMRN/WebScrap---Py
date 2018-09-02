# WebScrap-Py
This repo contains the script used by me to extract data out of webpages (web scraping) using a python script that I wrote using BeautifulSoup

# Introduction and Installing Package
Beautiful Soup is a Python library for pulling data out of HTML and XML files.

```
$ pip install beautifulsoup4.
```

# Package to Import
from urllib.request import urlopen  
from bs4 import BeautifulSoup  
import requests  
import re  

# Generalized function
Pass the website url you want to scrape in **pageUrl** and **your_criteria** is the condition based on which the webcrawling works  
###### Example
>Considering scraping of Wikipedia. Let the url be **"https://en.wikipedia.org/wiki/Web_scraping"** and if you want to crawl all the links in that particular page starts with  **"https://en.wikipedia.org/wiki/"** consider it  as **your_criteria** to do so.  

>What it does is, It find all the links that starts with **"https://en.wikipedia.org/wiki/"** and store it in a list and scrapping goes on.

```
scrapeurl (pageUrl):  
        global page  
        try:  
                r= requests.get(pageUrl)  
                html= r.text.encode("utf8")  
                soup = BeautifulSoup( html,'lxml')  
                links = soup.findAll('a', attrs={'href': re.compile("^your_criteria")})  
                for script in soup(["script", "style","nav","a"]):  
                        script.extract()  
                
                details = soup.body.text.strip()
                for s in details.split("\n"):
                    if s.strip():
                        print(s)
                
                for link in links:
                        if 'href' in link.attrs:
                                if link.attrs['href'] not in page:
                                        newPage = link.attrs['href']
                                        print(newPage)
                                        page.add(newPage)
                                        getLinks(newPage)
        except:
                pass
```
# User Agent

Some webpages will use the User Agent to display content that is customized to your particular browser. For example if your User Agent indicates you are using an old browser then the website may return the plain HTML version without any AJAX features, which may be easier to scrape.

Some websites will automatically block certain User Agents, for example if your User Agent indicates you are accessing their server with a script rather than a regular web browser.

Fortunately it is easy to set your User Agent to whatever you like by requesting with the header as follows

#### UserAgents List
```
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
  	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
]

```
You can find your own current **User Agent** [here](http://httpbin.org/get)

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




