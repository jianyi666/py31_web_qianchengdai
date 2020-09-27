#_*_coding:utf-8 -*-
#@Time     :2020/9/2722:34
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_login_case.py
#@Sotfware :PyCharm
from unittestreport import ddt,list_data
from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from data.login_data import login_data
import unittest
@ddt
class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        self.login_page= LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
    @list_data(login_data)
    def test_login(self,cases):
        # 登录输入账号密码进行登录
        self.login_page.login(cases["phone"],cases["pwd"])
        if cases['title'] == "登陆成功":
            res = self.index_page.get_my_account_ele()
            self.assertTrue(res)
        elif "为空" in cases['title']:
            none_ele_text = self.login_page.get_page_error_info()
            self.assertEqual(cases['expected'], none_ele_text)
        elif "错误" in cases['title'] or "未授权" in cases['title']:
            error_ele_text = self.login_page.get_toast_error_info()
            self.assertEqual(cases["expected"], error_ele_text)
    def tearDown(self):
        self.driver.quit()

