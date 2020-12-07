from selenium import webdriver
from selenium.webdriver.commom.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")

driver.get("http://newtours.demomoaut.com/")
user_ele=driver.find_element_by_name("username")
print(user_ele.is_displayed()) #returns true or false based on element status
print(user_ele.is_enabled()) #returns true or false

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed()) #returns true or false based on element status
print(pass_ele.is_enabled()) #returns true or false

user_ele.send_keys("mayuri")
pass_ele.send_keys("mayuri")
driver.find_element_by_name("login").click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print('status of round trip button is',roundtrip_radio.is_selected())#print status of the radio button

onetrip_radio=driver.find_element_by_css_selector("input[value=oneway]")
print('status of oneway button is',onetrip_radio.is_selected())#print status of the radio button