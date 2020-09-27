#_*_coding:utf-8 -*-
#@Time     :2020/9/2721:56
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :index_page.py
#@Sotfware :PyCharm
from selenium.webdriver.common.by import By
from locator.locators import Index
class IndexPage(object):
    def __init__(self,driver):
        self.driver = driver
    def get_my_account_ele(self):
        """获取我的账号ele"""
        try:
            self.driver.find_element(*Index.index_my_account_locator)
        except:
            return False
        else:
            return True