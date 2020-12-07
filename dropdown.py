from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element=driver.find_element_by_id("RESULT_RadioButton-7")
drp=select(element)

#select by visible text
drp.select_by_visible_text('Morning')

#select by index
drp.select_by_index(2) #afternoon

#select by value
drp.select_by_value("Radio-2")

#count tyhe number of options
print(len(drp.options))

#capture all the options and print them as output
all_options=drp.options
for options in all options:
    print(option.text)
    