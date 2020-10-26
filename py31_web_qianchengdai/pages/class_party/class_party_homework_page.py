#_*_coding:utf-8 -*-
#@Time     :2020/10/2322:43
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_homework_page.py
#@Sotfware :PyCharm
import time
from common.base_page import BasePage
from pywinauto.keyboard import send_keys
from locator.class_party.class_party_locators import ClassParty_HomeWork
class ClassPartyHomeWorkPage(BasePage):

    def HomeWork_Click_Updated_Submit(self):
        """
        点击选择文件后的，更新提交按钮
        :return:
        """
        time.sleep(1)
        self.click_ele(ClassParty_HomeWork.HomeWork_Updated_Submit_Button,"HomeWork页面，上传文件后点击更新提交")

    def HomeWork_Get_Task_Status(self):
        """
        获取作业的提交状态
        :return:
        """
        self.wait_ele_visibility(ClassParty_HomeWork.HomeWorK_Task_Upload_Status,"HomeWork页面，作业提交状态")
        return self.get_ele_text(ClassParty_HomeWork.HomeWorK_Task_Upload_Status,"HomeWork页面，作业提交状态")

    def HomeWork_Click_Levae_Message(self):
        """
        点击留言
        :return:
        """
        self.wait_ele_presence(ClassParty_HomeWork.HomeWork_Leave_Message,"HomeWork页面,留言")
        self.click_ele(ClassParty_HomeWork.HomeWork_Leave_Message,"HomeWork页面,留言")
    def HomeWork_Input_Levae_Message(self,value):
        """
        输入留言信息
        :param value:
        :return:
        """
        self.wait_ele_visibility(ClassParty_HomeWork.HomeWork_Input_Leave_Message,"HomeWork页面，输入留言")
        self.input_ele_sendkeys(ClassParty_HomeWork.HomeWork_Input_Leave_Message,value,"HomeWork页面，输入留言")
    def HomeWork_Click_Levae_Message_Kept(self):
        """
        点击保存留言
        :return:
        """
        self.wait_ele_clickable(ClassParty_HomeWork.HomeWork_Kept_Levae_Message,"HomeWork页面,保存按钮")
        self.click_ele(ClassParty_HomeWork.HomeWork_Kept_Levae_Message,"HomeWork页面,保存按钮")
    def HomeWork_Upload_Task(self,flies):
        """
        第一次上传作业
        :return:
        """
        self.wait_ele_presence(ClassParty_HomeWork.HomeWork_Add_task,"HomeWork页面，添加作业")
        self.click_ele(ClassParty_HomeWork.HomeWork_Add_task,"HomeWork页面，添加作业")
        time.sleep(1)
        send_keys(flies)
        send_keys("{VK_RETURN}")


    def HomeWork_Click_Upload_Button(self):
        """
        点击提交按钮
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_Upload,"HomeWork页面，提交按钮")

    def HomeWork_Get_Upload_Success_Text(self):
        """
        获取作业上传成功，提示信息
        :return:
        """
        self.wait_ele_visibility(ClassParty_HomeWork.HomeWork_System_Prompt_submit_success,"HomeWork页面,作业上传成功提示信息")
        return self.get_ele_text(ClassParty_HomeWork.HomeWork_System_Prompt_submit_success,"HomeWork页面,作业上传成功提示信息")
    def HomeWork_Click_Upload_Success_Know_Button(self):
        """
        点击上传作业成功提示框，我知道了按钮
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_System_Prompt_Know,"HomeWork页面，上传文件成功，我知道了按钮")

    def HomeWork_Click_Th_Task_Discuss(self):
        """
        点击表头，作业讨论
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_Task_Discuss,"HomeWork页面，表头作业讨论")
    def HomeWork_Input_Discuss_Text(self,value):
        """
        输入作业讨论内容
        :param value:
        :return:
        """
        self.input_ele_sendkeys(ClassParty_HomeWork.HomeWork_Add_comments,value,"HomeWork页面,输入作业讨论内容")
    def HomeWork_Click_Task_Discuss_Confirm(self):
        """
        作业讨论内容，提交
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_Confirm,"HomeWork页面,输入讨论内容后确定")
    def HomeWork_Click_Task_Discuss_Cancel(self):
        """
        作业讨论内容，取消
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_Cancel,"HomeWork页面,输入讨论内容后取消")
    def HomeWork_Get_Task_Upload_Status(self):
        """
        获取作业提交状态
        :return:
        """
        return self.get_ele_text(ClassParty_HomeWork.HomeWork_View_Task_Status,"HomeWork页面,作业提交状态")
    def HomeWork_Click_Update_Submit_Button(self):
        """
        点击更新提交按钮
        :return:
        """
        self.wait_ele_visibility(ClassParty_HomeWork.HomeWork_Update_Submit_Button,"HomeWork页面,更新提交按钮")
        self.click_ele(ClassParty_HomeWork.HomeWork_Update_Submit_Button,"HomeWork页面,更新提交按钮")
    def HomeWork_Click_Update_Frame_Ok_Button(self):
        """
        点击更新作业，提示框确定按钮
        :return:
        """
        self.wait_ele_clickable(ClassParty_HomeWork.HomeWork_Update_Work_Frame_OK_Button,"HomeWork页面,更新作业弹框确定按钮")
        self.click_ele(ClassParty_HomeWork.HomeWork_Update_Work_Frame_OK_Button,"HomeWork页面,更新作业弹框确定按钮")
    def HomeWork_Click_Update_Frame_Cancel_Button(self):
        """
        点击更新作业，提示框取消按钮
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_Update_Work_Frame_Cancel_Button,"HomeWork页面,更新作业弹框取消按钮")
    def HomeWork_Click_Delete_Task(self):
        """
        点击删除作业
        :return:
        """
        self.click_ele(ClassParty_HomeWork.HomeWork_Delete_Work,"HomeWork页面,删除作业")