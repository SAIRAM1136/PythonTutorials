#******************Commands************************
# get(Application commands)
# Conditional
# browser
# navigational
# wait
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#App commands : get, title, current_url, page_source
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)

#Conditional Commands: is_displayed, is_enabled, is_selected
# driver.get("https://demo.nopcommerce.com/register")
# driver.maximize_window()
#
# #is_displayed
# search_box=driver.find_element(By.ID,"small-searchterms").is_displayed()
# print("Display Status: ",search_box)
#
# #is_Enabled
# search_box=driver.find_element(By.ID,"small-searchterms").is_enabled()
# print("Enable Status: ",search_box)
#
# #is_selected : for radio buttons & check boxes
# radio_button=driver.find_element(By.ID, "gender-male").is_selected()
# print("Selected Status: ",radio_button)
# driver.find_element(By.ID, "gender-male").click()

#Browser Commands : close[it will close the tab which we opened in beginning] , quit
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element(By.XPATH, "//a[contains(text(),'OrangeHRM, Inc')]").click()
# print(driver.title)
# time.sleep(3)
#
# # driver.close()
# driver.quit()

#Navigational Commands : back, forward, refesh
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()
driver.forward()
driver.refresh()

driver.quit()





