#***************************XPATH**************************
#Relative Xpath SYNTAX: //tagname[@attribute='value']
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

#XPATH FOR I'm Feeling Lucky in Google search
# driver.get("https://www.facebook.com/")
driver.get("https://www.google.com/")
#driver.find_element(By.XPATH,'//div[@class="FPdoLc lJ9FBc"]//input[@class="RNmpXc"]').click()

#writting Xpath for Search button in google search box
driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys("Python")
# driver.find_element(By.XPATH,"//span[@class='QCzoEc z1asCe MZy1Rb']").click()
driver.find_element(By.XPATH,"//span[@class='QCzoEc z1asCe MZy1Rb']//*[name()='svg']").click()

time.sleep(3)

#OR AND USED WITH XPATH
# driver.find_element(By.XPATH,"//input[@id='email' or @name='email']]").send_keys("Python")
# driver.find_element(By.XPATH, "//input[@id='email' and @name='email']").send_keys("abc@gmail.com")

#Contains & starts with
# driver.find_element(By.XPATH, "//input[contains(@id,'pass')]").send_keys("abc123")
# driver.find_element(By.XPATH,"//input[starts-with(@id,'pass')]").send_keys("abc123")

#Text
# driver.find_element(By.XPATH, "//a[text()='Forgotten password?']").click()

