import time
from selenium import webdriver
from selenium.webdriver.common.by import By
totalrating =0
count = 1;
def init_driver():
    driver = webdriver.Chrome()
    return driver
 
def scrap(driver,query):
    driver.get("http://www.google.com/search?q="+query)
    links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")
    try:
        rating = driver.find_elements_by_class_name('slp f')
        for rates in rating:
            print(rates.text)

    except:
        pass
    
    contents = driver.find_elements_by_class_name('st')
    results = []
    for link,content in zip(links,contents):
        heading = link.text
        url = link.get_attribute('href')    
        print("\n{\n\"title\":"+heading+"\n\"url\":"+url+"\n\"content\":"+content.text+"\n}")
       
driver = init_driver()
scrap(driver,"HDFC reviews and ratings")
driver.quit()
