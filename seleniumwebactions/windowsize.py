from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://letskodeit.teachable.com")
driver.implicitly_wait(3)
height = driver.execute_script("return window.innerHeight")
width = driver.execute_script("return window.innerWidth")
print("Height is  :- " + str(height))
print("width is :- " + str(width))
driver.maximize_window()
heightafter = driver.execute_script("return window.innerHeight")
widthafter = driver.execute_script("return window.innerWidth")
print("Height is  :- " + str(heightafter))
print("width is :- " + str(widthafter))
driver.quit()
