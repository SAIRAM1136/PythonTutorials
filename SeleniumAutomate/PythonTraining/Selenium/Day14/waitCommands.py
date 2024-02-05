from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10) #**********IMPLICIT WAIT**************


#**********EXPLICIT WAIT**************
#mywait=WebDriverWait(driver, 10) #Explicit wait declaration
mywait=WebDriverWait(driver, 10,ignored_exceptions=[Exception])

driver.get("https://www.google.com/")
driver.maximize_window()

search_box=driver.find_element(By.NAME, 'q')

search_box.send_keys("Selenium")
search_box.submit()
#driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()

searchlink=mywait.until(EC.presence_of_element_located(By.XPATH,'//a[@href="https://www.selenium.dev/"]//h3[@class="LC20lb MBeuO DKV0Md"][normalize-space()="Selenium"]'))

searchlink.click()
















