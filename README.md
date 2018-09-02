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

# Beautiful Soup VS Selenium
```
####Static Scraping vs. Dynamic Scraping
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




