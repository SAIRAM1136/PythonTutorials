from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#Click on Links
driver.find_element(By.LINK_TEXT,'Digital downloads').click()
#driver.find_element(By.PARTIAL_LINK_TEXT, 'Digital').click()

#find number of links in a page
links=driver.find_elements(By.TAG_NAME,'a')
# links=driver.find_elements(By.XPATH,'//a')
print(len(links))

# print all links text
for i in links:
    print(i.text)

