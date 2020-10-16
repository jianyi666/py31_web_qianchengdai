import pytest
from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from pages.invest_page import InvestPage
from pages.user_page import Userpage

@pytest.fixture(scope='class')
def Login_SetUp():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get("http://120.78.128.25:8765/Index/login.html")
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page,index_page
    driver.quit()



@pytest.fixture(scope='class')
def Invest_SetUp():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get("http://120.78.128.25:8765/Index/login.html")
    login_page= LoginPage(driver)
    login_page.login("18684720553","python")
    index_page = IndexPage(driver)
    index_page.rush_to_did()
    invest_page = InvestPage(driver)
    user_page = Userpage(driver)
    yield invest_page,user_page
    driver.quit()

