#_*_coding:utf-8 -*-
#@Time     :2020/10/2220:04
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_index_page.py
#@Sotfware :PyCharm
import time
from  common.base_page import BasePage
from locator.class_party.class_party_locators import ClassParty_Index
class ClassPartyIndexPage(BasePage):


    def Index_Get_Join_Class_Error_Tips(self):
        """
        获取加入课程的错误提示信息
        :return:
        """
        time.sleep(0.5)
        return self.get_ele_text(ClassParty_Index.Index_Join_Course_Error_Tips,"Index页面，加入课程错误提示")


    def Index_Find_Login_User(self):
        """
        确认客户号已经登录
        :return:
        """
        self.wait_ele_presence(ClassParty_Index.Index_user,"Index页面，已登录")
        return self.find_ele(ClassParty_Index.Index_user,"Index页面，已登录")

    def Index_Click_Join_Class(self):
        """
        加入课程
        :return:
        """
        # 点击加入课程
        self.wait_ele_presence(ClassParty_Index.Index_Join_Course,"点击Index页面,加入课程")
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
        self.wait_ele_visibility(ClassParty_Index.Index_Frame_Cancel,"Index页面加入课堂弹框，点击取消")
        self.click_ele(ClassParty_Index.Index_Frame_Cancel,"Index页面加入课堂弹框，点击取消")

    def Index_Click_Into_Class(self):
        """
        Index页面加入课堂
        :return:
        """
        self.wait_ele_presence(ClassParty_Index.Index_Into_Class,"Index页面，进入课程")
        self.click_ele(ClassParty_Index.Index_Into_Class,"Index页面，进入课程")

    def Index_Click_Class_More(self):
        """
        Index页面，点击课程更多
        :return:
        """
        time.sleep(1)
        self.click_ele(ClassParty_Index.Index_Class_More,"Index页面,点击课程更多")

    def Index_Click_Class_Quit(self):
        """
        Index页面，点击课程更多后，退课
        :return:
        """
        self.wait_ele_visibility(ClassParty_Index.Index_Class_Quit,"Index页面，点击更多中的退课")
        self.click_ele(ClassParty_Index.Index_Class_Quit,"Index页面，点击更多中的退课")

    def Index_Class_Frame_Input_PassWord(self,value):
        """
        Index页面，退课弹框输入密码
        :return:
        """
        time.sleep(1)
        self.input_ele_sendkeys(ClassParty_Index.Index_Frame_Login_PassWord,value,"Index页面，退课弹框输入登录密码")

    def Index_Click_Class_Frame_Quit(self):
        """
        Index页面，点击退课弹框中退出
        :return:
        """
        time.sleep(1)
        self.wait_ele_clickable(ClassParty_Index.Index_Class_Frame_Quit,"Index页面，点击退课弹框中的退出")
        self.click_ele(ClassParty_Index.Index_Class_Frame_Quit,"Index页面，点击退课弹框中的退出")

    def Index_Click_Class_Frame_Cancel(self):
        """
         Index页面，点击退课弹框中的取消
        :return:
        """
        self.wait_ele_clickable(ClassParty_Index.Index_Class_Frame_Cancel, "Index页面，点击退课弹框中的取消")
        self.click_ele(ClassParty_Index.Index_Class_Frame_Cancel, "Index页面，点击退课弹框中的取消")

    def Index_Get_PassWord_Error_Toast_Text(self):
        """
        获取退课时输入错误密码返回的Toast提示信息
        :return:
        """
        return self.get_ele_text(ClassParty_Index.Index_Toast_PassWord_Error,"Index页面，获取退课时输入错误密码返回的Toast提示信息")

    def Index_Get_Join_OR_Drop_Class_Toast_Text(self,Join_Or_Drop):
        """
        获取加入和退出课程成功时的Toast提示信息
        :return:
        """
        time.sleep(0.5)
        return self.get_ele_text(ClassParty_Index.Index_Toast_Join_And_Drop_Class_Success,f"Index页面，获取{Join_Or_Drop}成功时的Toast提示信息")


