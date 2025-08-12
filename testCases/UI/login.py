import pytest
from pageObjects.loginPage import LoginPage
from testCases.UI.configTest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class TestLoginPage:

    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    path = ".//TestData/loginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("*********Testing home page**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        self.driver.close()

        if act_title == "nopCommerce demo store.Login":
            print("Title matches expected value.")
            self.logger.info("*********Passed home page**************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..\\screenshots\\" + "test_homePageTitle.png")
            print("Assertion failed: Actual title was '{act_title}'")
            self.logger.info("*********Failed home page**************")
            self.driver.close()
            assert False

    def test_login(self,setup): #Test Name should start with test_shfdb
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserEmail(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLoginButton()
       # self.driver.title

    # Reading from a file username, pwd
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)

            #contniue with above steps to login
