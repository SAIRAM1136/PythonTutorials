#driver.switch_to.alert
#text()
#accept()
#dismiss()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
#
# #Open alerts window
# driver.find_element(By.XPATH, "//button[text()= 'Click for JS Prompt']").click()
# time.sleep(5)
#
# #switch to pop up/ alert window
# alert_window = driver.switch_to.alert
# print(alert_window.text)
#
# alert_window.send_keys("Hello Selenium")
# #alert_window.accept() # used this command to click on okay
# alert_window.dismiss() # used this command to click on Cancel
# time.sleep(3)

#Example 2:
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
Pop_Up = driver.switch_to.alert
print(Pop_Up.text)
Pop_Up.accept()

