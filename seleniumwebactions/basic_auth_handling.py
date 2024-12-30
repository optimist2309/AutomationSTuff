"""
# What is Basic Auth ?
Basic Authentication is a method for an HTTP user agent (e.g., a web browser) to provide a
username and password when making a request.

When employing Basic Authentication, users include an encoded string in the Authorization header
of each request they make. The string is used by the request's
recipient to verify users' identity and rights to access a resource.

"""
# Below is the code snippet how to handle auth in python-selenium.
# https://the-internet.herokuapp.com/basic_auth
#https://username:password@your_website_url


import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)
driver.maximize_window()
text_box_element = driver.find_element(By.TAG_NAME, "p")
print(text_box_element.text)
time.sleep(5)
driver.quit()







