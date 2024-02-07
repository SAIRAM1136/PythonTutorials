import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#1) Select specific checkbox
driver.find_element(By.ID,'male').click()
time.sleep(5)

#2) Select all checkboxes at a time
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
print(len(checkBoxes))

#Approch 1
# for i in range(len(checkBoxes)):
#     checkBoxes[i].click()

#Approch 2
for i in checkBoxes:
    i.click()

#3) Select multiple checkboxes at a time of user's choice
# for i in checkBoxes:
#     weekname= i.get_attribute('id')
#     if weekname=='monday' or weekname=='thursday':
#         i.click()

#4)select last 2 checkboxes at a time

#range(7-2,7)-->(5,7) --->6,7
#total number of elements-2 = starting index
# for i in range(len(checkBoxes)-2, len(checkBoxes)):
#     checkBoxes[i].click()

#5)select first 2 checkboxes at a time
# for i in range(len(checkBoxes)):
#     if i <2:
#         checkBoxes[i].click()


#clear all check boxes
for i in checkBoxes:
    if i.is_selected():
        i.click()
