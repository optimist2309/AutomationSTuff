import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Calendar handling is tricky task for selenium automation . There are different ways to calendar handling.
For this example I am using click function.
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

# I do not know why this is not working,
#wait = WebDriverWait(driver, 20)
#wait.until(EC.visibility_of_element_located((By.ID, "ui-datepicker-div")))

driver.find_element(By.ID, "third_date_picker").click()
drop_down_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
drop_down_month_sel = Select(drop_down_month)
drop_down_month_sel.select_by_visible_text("Mar")
time.sleep(6)

drop_down_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
drop_down_year = Select(drop_down_year)
drop_down_year.select_by_visible_text("2025")

driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[text()='23']").click()
time.sleep(10)
driver.quit()
