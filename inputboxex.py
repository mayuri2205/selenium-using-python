from selenium import webdriver
from selenium.webdriver.commom.by import By
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#How to find how many inputboxes present in the web page
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

status=driver.find_element(By.ID,'RESULT_Textfield-1').is_displayed()
print("Displayed or not:",status)

status=river.find_element(By.ID,'RESULT_Textfield-1').is_enabled()
print("Enabled or not:",status)
#How to provide value into textbox
driver.find_element(By.ID,'RESULT_Textfield-1').send_keys("mayuri")
driver.find_element(By.ID,'RESULT_Textfield-2').send_keys("shinde")
driver.find_element(By.ID,'RESULT_Textfield-3').send_keys("12365")
