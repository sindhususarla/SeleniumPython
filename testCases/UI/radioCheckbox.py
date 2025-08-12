
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#Radio button
driver.find_element(By.XPATH, "//input[@value='Male']").click()

#Get all checkboxes and get attribute
li = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for element in li:
    val = element.get_attribute("value")
    if val == "Cricket":
        element.click()


#DROPDOWNS
select_web = driver.find_element(By.ID, 'Skills')

sel = Select(select_web)

sel.select_by_index(5)
sel.select_by_value('Configuration')
sel.select_by_visible_text('Design')

#Go to new url
driver.get('https://www.google.com/')

#Go back
driver.back()

#refresh
driver.refresh()

#forward
driver.forward()

#close browser
driver.quit()

driver.maximize_window()
driver.minimize_window()

