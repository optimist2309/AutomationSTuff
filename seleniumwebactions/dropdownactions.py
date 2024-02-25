import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

"""
In selenium if we have to handle dropdown elements for that thing select class is there.
Select class only works for HTML elements select and option. 
It is possible to design drop-downs with JavaScript overlays using div or li, and this class will not work for those.

"""
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

# First locate a <select> element, then use it to initialize a Select object.
# Note that as of Selenium 4.5, you can’t create a Select object if the <select> element is disabled.
select_element = driver.find_element(By.ID, 'dropdown')
select = Select(select_element)

# Get a list of all options in the <select> element:
option_list = select.options

# Getting all the options
opts = []
for each in option_list:
    opts.append(each.text)
print(opts)

# Get a list of selected options in the <select> element. For a standard select list this will only be a list with
# one element, for a multiple select list it can contain zero or many elements.
selected_option_list = select.all_selected_options

# The Select class provides three ways to select an option.
# Note that for multiple select type Select lists, you can repeat these methods for each element you want to select

# Text :- Select the option based on its visible text
select.select_by_visible_text('Option 2')

# Value :- Select the option based on its value attribute
select.select_by_value('1')

# Index
select.select_by_index(1)

# De-select option :_ Only multiple select type select lists can have options de-selected. You can repeat these
# methods for each element you want to select.
# select.deselect_by_value('eggs')

time.sleep(4)
driver.quit()
