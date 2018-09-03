import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def init_driver():
    driver = webdriver.Chrome()
    return driver
 
def scrap(driver,query):
    driver.get("http://www.google.com/search?q="+query)
    links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")
    contents = driver.find_elements_by_class_name('st')
    results = []
    for link,content in zip(links,contents):
        heading = link.text
        url = link.get_attribute('href')    
        print("Title:"+heading+"\n\"Url:"+url+"\n\Content:"+content.text+"\n")
       
driver = init_driver()
scrap(driver,"Selenium")
driver.quit()
