from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) #title of the page
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
#driver.close()#close the currentle focused browser
driver.quit()#close all the browsers