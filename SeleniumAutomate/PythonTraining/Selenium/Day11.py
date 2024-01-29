import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
#
# time.sleep(3)
# driver.find_element(By.NAME,'username').send_keys('Admin')
# driver.find_element(By.NAME,'password').send_keys('admin123')
# driver.find_element(By.XPATH,'//button[@type="submit"]').click()
#
# time.sleep(5)
# Actual_title=driver.title
# Expected_title='OrangeHRM'
#
# if Actual_title==Expected_title:
#     print("Login test is Passed")
# else:
#     print("Login test is Failed")
#
# driver.close()


#Example 2
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

time.sleep(3)
driver.find_element(By.ID,'Email').clear()
driver.find_element(By.ID,'Email').send_keys('admin@yourstore.com')
driver.find_element(By.ID,'Password').clear()
driver.find_element(By.ID,'Password').send_keys('admin')

driver.find_element(By.XPATH,'//button[@type="submit"]').click()

time.sleep(5)
Act_title=driver.title
Exp_title='Dashboard / nopCommerce administration'

if Act_title==Exp_title:
    print("Login test is Passed")
else:
    print("Login test is failed")

time.sleep(3)

driver.close()