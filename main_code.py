# import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#create empties

links = []
temp_context = []
translate = []
n_temp_context = []
n_translate = []

# detect webpage

driver = webdriver.Chrome()
page = driver.get("https://www.classcentral.com/") 

# crawl all page data 

source = driver.page_source

# collect text and webpages
span = driver.find_elements(By.TAG_NAME,'span')
h2 = driver.find_elements(By.TAG_NAME,'h2')
h3 = driver.find_elements(By.TAG_NAME,'h3')
h4 = driver.find_elements(By.TAG_NAME,'h4')
h5 = driver.find_elements(By.TAG_NAME,'h5')
a = driver.find_elements(By.TAG_NAME,'a')
href = driver.find_elements(By.XPATH ,"//a[@href]")

#generate text and webpage lists

for word in span and h2 and h3 and h4 and h5 and a:
    temp_context.append(word.text)

for link in href:
    links.append(link.get_attribute("href"))

context = [x for x in temp_context if x != ""]

#translate

leng = len(context)

google_translate = driver.get("https://translate.google.com/?hl=en&sl=en&tl=hi&op=translate") 
text = driver.find_element(By.TAG_NAME,'textarea')

for word in range(leng):
    text.send_keys(context[word])
    text.send_keys(Keys.ENTER)
    time.sleep(5)
    tra = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span')
    translate.append(tra.text)
    text.send_keys(Keys.CONTROL+"A")
    text.send_keys(Keys.DELETE)

# change the html code

for element in range(0, leng):
    new = source.replace(context[element],translate[element])
    source = new

new_source = source.replace('lang="en"','lang="hi"')

#create a document 
#       This is the part that I am incredibly unsuccessful

#loop the same process for the other webpages

for link in links:
    web_page = driver.get(link)
    source_code = driver.page_source

    n_span = driver.find_elements(By.TAG_NAME,'span')
    n_h2 = driver.find_elements(By.TAG_NAME,'h2')
    n_h3 = driver.find_elements(By.TAG_NAME,'h3')
    n_h4 = driver.find_elements(By.TAG_NAME,'h4')
    n_h5 = driver.find_elements(By.TAG_NAME,'h5')
    n_a = driver.find_elements(By.TAG_NAME,'a')

    for word in span and h2 and h3 and h4 and h5 and a:
        n_temp_context.append(word.text)
    n_context = [x for x in temp_context if x != ""]

    n_leng = len(n_context)
    google_translate = driver.get("https://translate.google.com/?hl=en&sl=en&tl=hi&op=translate") 
    text = driver.find_element(By.TAG_NAME,'textarea')

    for word in range(leng):
        text.send_keys(context[word])
        text.send_keys(Keys.ENTER)
        time.sleep(5)
        tra = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span')
        n_translate.append(tra.text)
        text.send_keys(Keys.CONTROL+"A")
        text.send_keys(Keys.DELETE)

    for element in range(0, n_leng):
        n_new = source.replace(n_context[element],n_translate[element])
        source_code = new


    
