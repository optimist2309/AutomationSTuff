from selenium.webdriver.common.by import By
from selenium import webdriver
"""
To get the text from a web element we can use text property and get the value.
Some times text property will not work for some elements in that case we can use get_attribute("value"). 
"""
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/abtest")
driver.maximize_window()
element_dd = driver.find_element(By.XPATH, "//p")
text_from_the_element = element_dd.text
print(text_from_the_element)
driver.quit()

