import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

#************* TO DISBALE NOTIFICATION POPUP*************
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=serv_obj, options=ops)

driver.get("https://whatmylocation.com/#google_vignette")

driver.maximize_window()



