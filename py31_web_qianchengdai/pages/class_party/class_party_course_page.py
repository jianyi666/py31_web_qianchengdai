#_*_coding:utf-8 -*-
#@Time     :2020/10/2322:45
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_course_page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.class_party.class_party_locators import ClassParty_Course
class ClassPartyCoursePage(BasePage):

    def click_task_name(self):
        """
        点击作业名称，进作业详情页面
        :return:
        """
        self.click_ele(ClassParty_Course.Course_Task_Name,"Course页面，作业名称，进入作业详情页面")

    def click_upload_task(self):
        """
        点击上传作业按钮
        :return:
        """
        self.click_ele(ClassParty_Course.Course_Upload_task,"Course页面，上传作业按钮")

    def click_subitted_button(self):
        """
        点击已提交按钮
        :return:
        """
        self.click_ele(ClassParty_Course.Course_Submitted_Button,"Course页面，已提交按钮")

    def click_th_task(self):
        """
        点击表头中作业
        :return:
        """
        self.click_ele(ClassParty_Course.Course_Task,"Course页面，表头中作业项")