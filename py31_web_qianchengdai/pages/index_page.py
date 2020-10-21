#_*_coding:utf-8 -*-
#@Time     :2020/9/2721:56
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :index_page.py
#@Sotfware :PyCharm
from locator.locators import Index
from common.base_page import BasePage
import time
class IndexPage(BasePage):

    def get_my_account_ele(self):
        """获取我的账号ele"""
        try:
            self.find_ele(Index.index_my_account_locator,"登陆成功！我的账号")
        except:
            return False
        else:
            return True
    def get_out(self):
        """退出登录"""
        try:
            self.click_ele(Index.index_get_out_locator,"退出登录")
        except:
            return False
        else:
            return True
    def get_in(self):
        """点击登陆"""
        try:
            self.click_ele(Index.index_get_in_locator,"点击登陆")
        except:
            return False
        else:
            return True

    def rush_to_did(self):
        """抢投标"""
        time.sleep(0.5)
        self.click_ele(Index.index_rush_to_bid,"点击抢投标按钮")