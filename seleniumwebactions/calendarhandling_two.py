import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

"""
Calendar handling is tricky task for selenium automation . There are different ways to calendar handling.
So in this example sendkeys() function is getting used.
I have  used too much time.sleep() in future I will optimise this code.
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/")
driver.find_element(By.NAME, "bdaytime").send_keys("11252025")
time.sleep(7)
driver.find_element(By.NAME, "bdaytime").send_keys(Keys.TAB)
time.sleep(5)
driver.find_element(By.NAME, "bdaytime").send_keys("1050")
time.sleep(6)
driver.find_element(By.NAME, "bdaytime").send_keys("PM")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(10)
driver.quit()
