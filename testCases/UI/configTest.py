from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#  pytest -s -v testCases/login.py --browser chrome
# pytest -s -v -n=2 testCases/login.py --browser chrome ==== login has 2 tests and both will run in two different chrome browsers at the same time
#pytest -s -v -m "sanity or regression" testCases/login
#OR create run.bat file

#  pytest -s -v --html=report.html testCases/login.py --browser chrome