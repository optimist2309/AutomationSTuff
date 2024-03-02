import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letskodeit.teachable.com")
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
driver.find_element(By.ID, "user_password").send_keys("abc")
driver.find_element(By.NAME, "commit").click()
destinationFileName = "C:\\Users\\haris\\Downloads\\test.png"
try:
    driver.save_screenshot(destinationFileName)
    print("Screenshot saved to directory --> :: " + destinationFileName)
except NotADirectoryError:
    print("Not a directory issue")
time.sleep(2)
driver.quit()