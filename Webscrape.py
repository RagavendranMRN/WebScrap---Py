from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import random
import re
page = set()
def scrapeurl(pageUrl):
        global page
        try:
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
                r= requests.get(pageUrl, headers=headers)
                html= r.text.encode("utf8")
                soup = BeautifulSoup( html,'lxml')
                links = soup.findAll('a', attrs={'href': re.compile("^https://en.wikipedia.org/wiki/")})
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
        
scrapeurl("https://en.wikipedia.org/wiki/Web_scraping”)

