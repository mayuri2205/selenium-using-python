from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
#driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver=webdriver.Firefox(executable_path="C:\Program Files\Mozilla Firefox\firefox.exe")
driver.get("http://newtours.demomoaut.com/")
print(driver.title) #title of the page
print(driver.current_url)#returns the url of the page
print(driver.page_source)#HTML code for the page
driver.close()#close the browser