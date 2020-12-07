from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver.get("http://newtours.demomoaut.com/")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)