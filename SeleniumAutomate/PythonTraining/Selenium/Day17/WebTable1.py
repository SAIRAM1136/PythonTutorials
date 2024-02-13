import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1) Count number of rows and columns
rows=driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print(len(rows))

columns=driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
print(len(columns))

#2)Read specific row and column data
data=driver.find_element(By.XPATH, "//td[normalize-space()='Master In Selenium']").text
print(data)

#3)Read all rows and columns data
for i in range(2,rows+1):
    for j in range(1,columns+1):
        data=driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr["str(r)+"]/td["str(c)+"]').text
        print(data,end='    ')
    print()

#4)Read data based on condition
for r in range(2,rows+1):
    authorname=driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr["str(r)+"]/td[2]').text
    if authorname=='Mukesh':
        bookName=driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr["str(r)+"]/td[1]').text
        price = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr["str(r)+"]/td[4]').text
        print(bookName,"     ",authorname,"   ",price)






