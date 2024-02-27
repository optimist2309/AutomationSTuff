import time
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
To get the attribute value from any web-element we can use get_attribute() to get the value 
"""
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
text_box_element = driver.find_element(By.ID, "my-text-id")
text_box_element.send_keys("Hello How are you ?? ")
time.sleep(5)
text_box_value = text_box_element.get_attribute("value")
print(text_box_value)
driver.quit()