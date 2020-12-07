from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")

driver.get("http://newtours.demomoaut.com/")#opening URL takes some time
driver.implicitly_wait(10)#second
assert "welcome :Mercury Tours" in driver.title
driver.find_element_by_name("username").send_keys("mayuri"
driver.find_element_by_name("password").send_keys("mayuri")
driver.find_element_by_name("login").click()
