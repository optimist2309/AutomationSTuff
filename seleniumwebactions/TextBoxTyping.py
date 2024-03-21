import time
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
To Enter the text into text box/password/textarea we have send_keys() function.
"""
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()

# Example of entering text into text box.
text_to_enter = 'Hey Smile You are amazing/awesome !!'
text_box_element = driver.find_element(By.ID, "my-text-id")
text_box_element.send_keys(text_to_enter)
time.sleep(5)

# Example of entering text into password text box.
text_box_element_pass = driver.find_element(By.NAME, "my-password")
text_box_element_pass.send_keys("ssssshhhhhHHH")
time.sleep(5)

# Example of entering text into text area.
text_to_enter_textarea = ("Hey Smile You are amazing/awesome \n"
                          "Have the day that you deserve !!!!")
text_area_element = driver.find_element(By.NAME, "my-textarea")
text_area_element.send_keys(text_to_enter_textarea)
time.sleep(5)
driver.quit()
