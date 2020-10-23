#_*_coding:utf-8 -*-
#@Time     :2020/10/2120:52
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_login_page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.class_party.class_party_locators import ClassParty_Login
class ClassPartyLoginPage(BasePage):

    def Index_Click_Logoin(self):
        """
        点击登录
        :return:
        """
        self.click_ele(ClassParty_Login.Login_Login,"Login页面登录")

    def Index_Close_Frame(self):

        self.click_ele(ClassParty_Login.Login_Frame_Close,"关闭Login页面提示弹框")

    def Index_Get_Into_Class(self):

        self.click_ele(ClassParty_Login.Login_Get_Into_Class,"Login页面进入课堂")
