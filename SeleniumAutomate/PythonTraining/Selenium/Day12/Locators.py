#***************************Locators******************************
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

#driver.get("https://demo.nopcommerce.com/")
driver.get("https://www.facebook.com/")
driver.maximize_window()

#Different types of Locators Examples:
# driver.find_element(By.ID,'small-searchterms').send_keys("Lenovo IdeaCentre 600 All-in-One PC")
# driver.find_element(By.XPATH,'//button[normalize-space()="Search"]').click()
# driver.find_element(By.LINK_TEXT,'Register').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()

#To capture total no of links in a webpage
# Tags=driver.find_elements(By.TAG_NAME,'a')
# print(len(Tags))

#CSS SELECTOR
#Tag & ID  : Syntax : tagname#valueOfId
# driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('abc')

#Tag & Class: syntax: tagname.valueOfClass
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('abc@gmail.com')

#Tag & Attribute : Syntax : tagname[attribute Along with Value]
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('abc@gmail.com')

#Tag,class&Attribute: Syntax : tagname.ValueOfClass[attribute=value]: when tagname & classname is matching with 2 elements we use this Locator
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name="pass"]').send_keys('123')


time.sleep(3)