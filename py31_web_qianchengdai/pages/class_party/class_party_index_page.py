#_*_coding:utf-8 -*-
#@Time     :2020/10/2220:04
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_index_page.py
#@Sotfware :PyCharm
from  common.base_page import BasePage
from locator.class_party.class_party_locators import ClassParty_Index
class ClassPartyIndexPage(BasePage):

    def Index_Click_Join_Class(self,value):
        """
        加入课程
        :return:
        """
        # 点击加入课程
        self.click_ele(ClassParty_Index.Index_Join_Course,"点击Index页面,加入课程")

    def Index_Input_Class_Code(self,value):
        """
        输入课程代码
        :param value:
        :return:
        """
        # 输入课程代码
        self.input_ele_sendkeys(ClassParty_Index.Index_Frame_Input_class_code,value,"Index页面输入课程代码")

    def Index_Click_Frame_Join(self):
        """
        Index页面加入课堂弹框，点击加入
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Frame_Join,"Index页面加入课堂弹框，点击加入")

    def Index_Click_Frame_Cancel(self):
        """
        Index页面加入课堂弹框，点击取消
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Frame_Cancel,"Index页面加入课堂弹框，点击取消")

    def Index_Click_Into_Class(self):
        """
        Index页面加入课堂
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Into_Class,"Index页面，进入课程")

    def Index_Click_Class_More(self):
        """
        Index页面，点击课程更多
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Class_More,"Index页面,点击课程更多")

    def Index_Click_Class_Quit(self):
        """
        Index页面，点击课程更多后，退课
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Class_Quit,"Index页面，点击更多中的退课")

    def Index_Class_Frame_Input_PassWord(self,value):
        """
        Index页面，退课弹框输入密码
        :return:
        """
        self.input_ele_sendkeys(ClassParty_Index.Index_Frame_Login_PassWord,value,"Index页面，退课弹框输入登录密码")

    def Index_Click_Class_Frame_Quit(self):
        """
        Index页面，点击退课弹框中退出
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Class_Frame_Quit,"Index页面，点击退课弹框中的退出")

    def Index_Click_Class_Frame_Cancel(self):
        """
         Index页面，点击退课弹框中的取消
        :return:
        """
        self.click_ele(ClassParty_Index.Index_Class_Frame_Cancel, "Index页面，点击退课弹框中的取消")
