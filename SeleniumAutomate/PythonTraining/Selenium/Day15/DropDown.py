import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.geodatasource.com/software/country-region-dropdown-menu-demo")
driver.maximize_window()
# driver.implicitly_wait(10)

time.sleep(10)
#dropdown_country=driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry=Select(driver.find_element(By.XPATH, "//select[@country-data-region-id='gds-cr-one']"))

#Select option from drop down
# drpcountry.select_by_visible_text("India")

# #Capture all the options and print
alloptions=drpcountry.options
print(len(alloptions))
# for i in alloptions:
#     print(i.text)

#Select option from dropdown without using built in method
for i in alloptions:
    if i.text == "India":
        i.click()
        break

        
