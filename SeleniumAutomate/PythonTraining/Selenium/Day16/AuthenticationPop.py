#Syntax to Inject Username and password inside URL :
#Example :https://admin:admin@the-internet.herokuapp.com/basic_auth
#https://username:password@the-internet.herokuapp.com/basic_auth

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://the-internet.herokuapp.com/basic_auth")

#Injected Username and password in URL
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()




