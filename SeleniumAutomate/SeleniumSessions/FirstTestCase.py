import time
from sys import executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, 'APjFqb').send_keys("naveen automationlabs")
option_list = driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li span')
print(len(option_list))

driver.implicitly_wait(5)

for ele in option_list:
    print(ele.text)
    if ele.text == "naveen automationlabs selenium interview questions":
        ele.click()
        break

time.sleep(5)
driver.quit()


