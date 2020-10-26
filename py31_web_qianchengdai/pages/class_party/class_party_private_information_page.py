#_*_coding:utf-8 -*-
#@Time     :2020/10/2517:55
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_private_information_page.py
#@Sotfware :PyCharm
import time
from common.base_page import BasePage
from locator.class_party.class_party_locators import ClassParty_PrivateInformation

class ClassPartyPrivateInformationPage(BasePage):


    def PrivateInformation_Click_Message_Input(self):
        """
        点击聊天输入框
        :return:
        """
        self.click_ele(ClassParty_PrivateInformation.PrivateInformation_Input_Text,"私信页面，点击输入框")
    def PrivateInformation_Click_Icon(self):
        """
        点击私信Icon
        :return:
        """
        self.click_ele(ClassParty_PrivateInformation.PrivateInformation_Icon,"私信Icon")


    def PrivateInformation_Click_Contacts(self):
        """
        私信页面点击联系人
        :return:
        """
        self.wait_ele_presence(ClassParty_PrivateInformation.PrivateInformation_Contacts,"PrivateInformation页面,联系人")
        self.click_ele(ClassParty_PrivateInformation.PrivateInformation_Contacts,"PrivateInformation页面,联系人")

    def PrivateInformation_Click_Py31_Class(self):
        """
        点击选择python自动化第31期
        :return:
        """
        self.wait_ele_visibility(ClassParty_PrivateInformation.PrivateInformation_Py31,"PrivateInformation页面,python自动化第31期")
        self.click_ele(ClassParty_PrivateInformation.PrivateInformation_Py31,"PrivateInformation页面,python自动化第31期")

    def PrivateInformation_Click_Choice_Contacts(self):
        """
        选择需要私信的联系人
        :return:
        """
        self.wait_ele_visibility(ClassParty_PrivateInformation.PrivateInformation_Choice_Contact,"PrivateInformation页面,选择丹丹发送私信")
        self.click_ele(ClassParty_PrivateInformation.PrivateInformation_Choice_Contact,"PrivateInformation页面,选择丹丹发送私信")

    def PrivateInformation_Input_Chat_Text(self,value):
        """
        输入聊天内容
        :param value:
        :return:
        """
        self.wait_ele_visibility(ClassParty_PrivateInformation.PrivateInformation_Input_Text,value,"PrivateInformation页面,输入聊天内容")
        self.input_ele_sendkeys(ClassParty_PrivateInformation.PrivateInformation_Input_Text,value,"PrivateInformation页面,输入聊天内容")

    def PrivateInformation_Click_Send_Out(self):
        """
        点击发送
        :return:
        """
        self.wait_ele_clickable(ClassParty_PrivateInformation.PrivateInformation_Send_Out,"PrivateInformation页面，点击发送")
        self.click_ele(ClassParty_PrivateInformation.PrivateInformation_Send_Out,"PrivateInformation页面，点击发送")
