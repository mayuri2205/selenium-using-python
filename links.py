from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver.get("http://newtours.demomoaut.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print("number of links present :",len(links))
for link in links:
    print(link.text)


#clicking on the link
driver.find_element(By.LINK_TEXT,"REGISTER").click()

