from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://imgbb.com/upload")
element = driver.find_element(By.ID, "anywhere-upload-input")
element.send_keys("/Users/atomar/Desktop/fileupload.png")
driver.quit()