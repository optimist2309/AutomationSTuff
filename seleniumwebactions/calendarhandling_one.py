import time

from selenium import webdriver

"""
Calendar handling is tricky task for selenium automation . There are different ways to calendar handling.
For this example I am using javascript executor to handle date operation.
This is not a correct way to handle calendar operation.
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.execute_script("document.getElementById('datepicker').value='25/11/2024'")
time.sleep(4)
driver.quit()
