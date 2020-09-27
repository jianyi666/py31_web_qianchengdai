#_*_coding:utf-8 -*-
#@Time     :2020/9/2721:56
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :login_page.py
#@Sotfware :PyCharm

from locator.locators import Login,Index
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
    def login(self,mobile_phone,pwd):
        # 输入登录账号
        self.driver.find_element(*Login.login_mobile_locator).send_keys(mobile_phone)
        # 输入登录密码
        self.driver.find_element(*Login.login_pwd_locator).send_keys(pwd)
        # 点击登录
        self.driver.find_element(*Login.login_button_locator).click()

    def get_page_error_info(self):
        page_error_ele_text = self.driver.find_element(*Login.login_page_error_locator).text
        return page_error_ele_text
    def get_toast_error_info(self):
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(Login.login_toast_error_locator))
        toast_error_ele_text = self.driver.find_element(*Login.login_toast_error_locator).text
        return toast_error_ele_text