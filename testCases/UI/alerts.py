from tkinter.font import names

from selenium.webdriver import Keys

#Alerts

#Accept alert
driver.switch_to.alert.accept()

#Alert with cancel
driver.switch_to.alert.dismiss()

#Verify alert text
alertText = driver.switch_to.alert.text
print(alertText)

#Enter text in alert
driver.switch_to.alert.send_keys("Yes")
driver.switch_to.alert.accept()


# NAVIGATE TO TABS

#parent window
parent_window = driver.current_window_handle


window = driver.window_handles

for win in window:
    if win != parent_window:
        driver.switch_to.window(win)

#Action in child window
driver.find_element(By.XPATH, "//*[contains(text(),'<UNK>')]").click()
driver.close()

driver.switch_to.window(parent_window)
driver.quit()


#FRAMES

#Using index
driver.switch_to.frame(0)

#Using name or id
driver.switch_to.frame("singleframe") # can be id or name

#element
driver.switch_to.frame(By.XPATH,"//div[@id='Single']/iframe")

driver.switch_to.default_content()




