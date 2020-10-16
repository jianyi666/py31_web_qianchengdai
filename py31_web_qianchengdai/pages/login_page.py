#_*_coding:utf-8 -*-
#@Time     :2020/9/2721:56
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :login_page.py
#@Sotfware :PyCharm

from locator.locators import Login,Index
from pages.base_page import BasePage
import time
class LoginPage(BasePage):

    def login(self,mobile_phone,pwd):
        # 输入登录账号
        self.input_ele_sendkeys(Login.login_mobile_locator,mobile_phone,"账号输入框")
        # 输入登录密码
        self.input_ele_sendkeys(Login.login_pwd_locator,pwd,"密码输入框")
        # 点击登录
        self.click_ele(Login.login_button_locator,"点击登陆")

    def get_page_error_info(self):
        self.wait_ele_visibility(Login.login_page_error_locator,"账号密码为空错误")
        return  self.get_ele_text(Login.login_page_error_locator,"账号密码为空错误文本")

    def get_toast_error_info(self):
        self.wait_ele_visibility(Login.login_toast_error_locator,"账号密码为空错误toast")
        time.sleep(0.5)
        return self.get_ele_text(Login.login_toast_error_locator,"账号密码为空错误文本")