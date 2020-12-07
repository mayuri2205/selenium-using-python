from selenium import webdriver
from selenium.webdriver.commom.by import By
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#working with radio button
status=driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()
print(status)

status=driver.find_element_by_id("RESULT_RadioButton-8_0").click() #select radio button

status=driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()
print(status)

#working with check boxes
driver.find_element_by_id("RESULT_CheckBox-9_0").click() #sunday
driver.find_element_by_id("RESULT_CheckBox-9_6").click() #saturday

status=driver.find_element_by_id("RESULT_CheckBox-9_0").is_selected()
print(status)