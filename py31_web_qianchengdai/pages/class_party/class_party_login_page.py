#_*_coding:utf-8 -*-
#@Time     :2020/10/2120:52
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_login_page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.class_party.class_party_locators import ClassParty_Login
import time
class ClassPartyLoginPage(BasePage):

    def Login_Click_Login(self):
        """
        点击登录
        :return:
        """
        time.sleep(0.5)
        self.click_ele(ClassParty_Login.Login_Login,"Login页面登录")

    def Login_Close_Frame(self):
        """
        关闭登录页面弹框
        :return:
        """
        self.wait_ele_visibility(ClassParty_Login.Login_Frame_Close,"Login页面提示弹框")
        self.click_ele(ClassParty_Login.Login_Frame_Close,"关闭Login页面提示弹框")

    def Login_Get_Into_Class(self):
        """
        登录页面，进入课堂
        :return:
        """

        self.click_ele(ClassParty_Login.Login_Get_Into_Class,"Login页面进入课堂")

    def Login_Input_Account(self,value):
        """
        登录页面，输入登录账号
        :return:
        """
        time.sleep(0.5)
        self.input_ele_sendkeys(ClassParty_Login.Login_Input_Account,value,"Login页面，账号输入框，输入账号")

    def Login_Input_PassWord(self,value):
        """
        登录页面，输入登录密码
        :param value:
        :return:
        """
        self.wait_ele_presence(ClassParty_Login.Login_Input_PassWord,"Login页面，账户输入框，输入密码")
        self.input_ele_sendkeys(ClassParty_Login.Login_Input_PassWord,value,"Login页面，账户输入框，输入密码")

    def Login_Click_Login_Button(self):
        """
        登录页面，点击登录按钮
        :return:
        """
        self.wait_ele_clickable(ClassParty_Login.Login_Login_Button,"Login页面，点击登录按钮")
        self.click_ele(ClassParty_Login.Login_Login_Button,"Login页面，点击登录按钮")

    def Login_Get_Login_Error_Text(self):
        """
        登录页面，获取登录错误信息
        :return:
        """
        return self.get_ele_text(ClassParty_Login.Login_Error_Tips,"Login页面，获取登录错误信息")
