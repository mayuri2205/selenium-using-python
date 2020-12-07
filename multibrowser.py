from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")

driver.get("http://newtours.demomoaut.com/")
print(driver.title) #title of the page
driver.close()#close the browser