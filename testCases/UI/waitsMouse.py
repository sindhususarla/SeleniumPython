from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Selenium is async calls

#implicit wait - when you wait for new page or async api call
driver.implicitly_wait(5)

#explicit wait
wait = WebDriverWait(driver,5)
wait.until(EC.visibility_of_element_located(By.XPATH,"//input[@id=' ']")).send_keys("Yes")

#MOUSE

#hover
element = driver.find_element_(By.XPATH,"//input[@id=' ']")

action = ActionChains(driver)
action.move_to_element(element).perform()

#move to and click
action.move_to_element(element).click().perform()
action.click(element).perform()

#KEYBOARD
action.key_down(Keys.SHIFT).send_keys("Test").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()



