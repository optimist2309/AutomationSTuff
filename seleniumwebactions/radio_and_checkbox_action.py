from selenium import webdriver
from selenium.webdriver.common.by import By

"""

To check and uncheck the radio button we can perform this action with click(),
We can check and uncheck of the checkboxes with the help of click().
is_selected method is used to check if element is selected or not. It returns a boolean value True or False.
It can be used to check if a checkbox or radio button is selected.

"""
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(by=By.XPATH, value="//a[@href='/checkboxes']").click()
driver.implicitly_wait(5)

chckboxbox1valuebfr= driver.find_element(by=By.XPATH, value="//form//input[1]").is_selected()
print("1st Check box value is "+ str(chckboxbox1valuebfr))
driver.find_element(by=By.XPATH, value="//form//input[1]").click()
driver.find_element(by=By.XPATH, value="//form//input[2]").click()

chckboxbox1valueafter= driver.find_element(by=By.XPATH, value="//form//input[1]").is_selected()
print("1st Check box value is "+ str(chckboxbox1valueafter))
driver.quit()


