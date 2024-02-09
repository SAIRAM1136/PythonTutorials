import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# windowID=driver.current_window_handle
# print(windowID) #6E51B3735E9A5BE1B3E9EC9B1BB4ED2E

time.sleep(5)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIDs = driver.window_handles

#Approch 1
# parent_window= windowIDs[0] #Parent_window
# child_window= windowIDs[1] #child_window
#
# driver.switch_to.window(child_window)
# print("Child window is : ",driver.title)
#
# driver.switch_to.window(parent_window)
# print("Parent Window is : ",driver.title)

#Approch 2 ****************imp*******************************

for i in windowIDs:
    driver.switch_to.window(i)
    print(driver.title)
    if driver.title== "OrangeHRM":
        driver.close()


