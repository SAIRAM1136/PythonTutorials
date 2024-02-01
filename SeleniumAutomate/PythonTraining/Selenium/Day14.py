#*****************************XPATH AXES**************************************
# Self,
# Parent,
# child,
# ancestor,
# descendant,
# following,
# following siblings,
# preceding
# Preceding-sibling

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\saira\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/indices/bse/bse100?src=moneyhome_bseIndices")
driver.maximize_window()

#self
# text_message=driver.find_element(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/self::a").text
# print(text_message)

#Parent
# print(text_msg)
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/parent::td").text

#child
# all_values=driver.find_elements(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr/child::td")
# print(len(all_values))

#Ancestor
# text_message=driver.find_element(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr").text
# print(text_message)

#descendant
# descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr/descendant::*")
# print(len(descendants))

#following
# followings=driver.find_elements(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr/following::*")
# print(len(followings))

#following-sibling
# following_siblings=driver.find_elements(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr/following-sibling::*")
# print(len(following_siblings))

#preceding
# preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr/preceding::tr")
# print(len(preceding))

#preceding-siblings
preceding_siblings=driver.find_elements(By.XPATH,"//a[contains(text(),'IndusInd Bank Ltd')]/ancestor::tr/preceding-sibling::tr")
print(len(preceding_siblings))

driver.close()
