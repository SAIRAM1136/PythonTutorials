#we need to install requests package through settings

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(10)

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0

for i in allLinks:
    url=i.get_attribute('href')
    try:
        response =requests.head(url)
    except:
        None

    if response.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,'is a valid link')

print("Total number of broken links:", count)