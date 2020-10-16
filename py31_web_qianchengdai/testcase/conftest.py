import pytest
from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.invest_page import InvestPage

@pytest.fixture(scope='class',autouse=True)
def Login_SetUp():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get("http://120.78.128.25:8765/Index/login.html")
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page,index_page
    driver.quit()

@pytest.fixture(scope='class',autouse=True)
def Invest_SetUp():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get("http://120.78.128.25:8765/Index/login.html")
    LoginPage.login("18684720553","python")
    IndexPage.rush_to_did()
    invest_page = InvestPage(driver)
    yield invest_page
    driver.quit()


