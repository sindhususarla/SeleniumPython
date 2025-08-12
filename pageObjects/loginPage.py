from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email = "//input[@type='email']"
    textbox_password = "//input[@type='password']"
    login_button = "//button[@type='submit']"
    logout_button = "//a[text()='Logout']"

    def __init__(self,driver) :
        self.driver = driver

    def setUserEmail(self,email) :
        self.driver.find_element(By.XPATH,self.textbox_email).clear()
        self.driver.find_element(By.XPATH,self.textbox_email).send_keys(email)

    def setUserPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password).clear()
        self.driver.find_element(By.XPATH,self.textbox_password).send_keys(password)

    def clickLoginButton(self) :
        self.driver.find_element(By.XPATH,self.login_button).click()

    def clickLogoutButton(self) :
        self.driver.find_element(By.XPATH,self.logout_button).click()

