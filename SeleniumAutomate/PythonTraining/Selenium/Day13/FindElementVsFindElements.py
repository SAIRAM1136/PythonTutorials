#****************find_element() & find_elements()**********************

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#find_element() : return single element

#Scenario 1 : Locator matching with single web element
# ele=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# ele.send_keys("Apple macbook Pro")

#Scenario 2 : Locator matching with multiple web elements
# ele=driver.find_element(By.XPATH,"//div[@class='footer']//a") #xpath is used to get all below links in a webpage
# print(ele.text)

#scenario 3: Element not available [NoSuchElementException: Message: no such element: Unable to locate element]
# ele=driver.find_element(By.LINK_TEXT, "Log ")
# ele.click()

#find_elements() : return multiple web element[returns LIST Collections]

#Scenario 1 : Locator matching with single web element
# ele=driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(ele))
# ele[0].send_keys("Apple macbook Pro")

#Scenario 2 : Locator matching with multiple web elements
# ele=driver.find_elements(By.XPATH,"//div[@class='footer']//a") #xpath is used to get all below links in a webpage
# print(len(ele))
#
# for i in ele:
#     print(i.text) #to print text of all links
# else:
#     print("Loop Ended")

#scenario 3: Element not available [NoSuchElementException: Message: no such element: Unable to locate element]
ele=driver.find_elements(By.LINK_TEXT, "Log ")
print(len(ele))

