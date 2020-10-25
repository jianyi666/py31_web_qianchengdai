#_*_coding:utf-8 -*-
#@Time     :2020/10/2521:18
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_class_party_index_page_case.py
#@Sotfware :PyCharm
import time
import pytest
from data.class_party.class_party_index_data import ClassParty_Index_Error_Data,\
    ClassParty_Index_Success_Data,ClassParty_Index_Repeat_Join_Data,ClassParty_Index_Into_Course_Data
class Test_ClassParty_IndexPageCase():

    @pytest.mark.parametrize("cases",ClassParty_Index_Error_Data)
    def test_Join_course_error_tips(self,cases,ClassParty_Index_fixture):
        index_page = ClassParty_Index_fixture[0]
        # 输入课程代码
        index_page.Index_Input_Class_Code(cases["code"])
        # 点击加入
        index_page.Index_Click_Frame_Join()
        #断言
        assert cases["Expect"] == index_page.Index_Get_Join_Class_Error_Tips()

    @pytest.mark.parametrize("cases",ClassParty_Index_Success_Data)
    def test_Join_Course_Sucess(self,cases,ClassParty_Index_fixture):
        index_page = ClassParty_Index_fixture[0]
        # 输入课程代码
        index_page.Index_Input_Class_Code(cases["code"])
        # 点击加入
        index_page.Index_Click_Frame_Join()
        # 断言
        assert cases["Expect"] == index_page.Index_Get_Join_OR_Drop_Class_Toast_Text("加入课程")

    @pytest.mark.parametrize("cases", ClassParty_Index_Repeat_Join_Data)

    def test_Repeat_Join_Course(self,cases,ClassParty_Index_fixture):
        index_page = ClassParty_Index_fixture[0]
        # 点击加入课程
        index_page.Index_Click_Join_Class()
        # 输入课程代码
        index_page.Index_Input_Class_Code(cases["code"])
        # 点击加入
        index_page.Index_Click_Frame_Join()
        # 断言
        assert cases["Expect"] == index_page.Index_Get_Join_Class_Error_Tips()
        # 关闭弹框
        index_page.Index_Click_Frame_Cancel()

    @pytest.mark.parametrize("cases", ClassParty_Index_Into_Course_Data)
    def test_Into_Course_Success(self,cases,ClassParty_Index_fixture):
        index_page,course_page = ClassParty_Index_fixture

        #点击进入课程
        index_page.Index_Click_Into_Class()
        # 断言
        assert cases['Expect'] == course_page.Course_Get_CourseCode()

