import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

#driver.switch_to.default_content : this command is used to navigate back from frame to web page
#driver.switch_to.frame("name1") #this command is to switch to the frame

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

OuterFrame=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(OuterFrame)

innerFrame=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH, "input[type='text']").send_keys("Welcome")

