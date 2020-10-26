import time
import pytest
from data.class_party.class_party_homework_data import ClassParty_HomeWork_Upload_Task_Data,ClassParty_HomeWork_Updata_Task_Data
class Test_ClassParty_CoursePage():

    # @pytest.mark.parametrize("cases",ClassParty_HomeWork_Upload_Task_Data)
    # def test_upload_task(self,cases,ClassParty_Course_fixture):
    #
    #     course_page,homework_page = ClassParty_Course_fixture
    #     #点击上传作业
    #     course_page.Course_Click_Upload_Task()
    #     # 选择文件进行上传
    #     homework_page.HomeWork_Upload_Task(cases["files"])
    #     # 点击留言
    #     homework_page.HomeWork_Click_Levae_Message()
    #     # 输入留言内容
    #     homework_page.HomeWork_Input_Levae_Message(cases["message"])
    #     # 点击保存
    #     homework_page.HomeWork_Click_Levae_Message_Kept()
    #     # 点击提交
    #     homework_page.HomeWork_Click_Upload_Button()
    #     # 断言
    #     assert cases["Expect"] == homework_page.HomeWork_Get_Upload_Success_Text()
    #     # 点击我知道了
    #     homework_page.HomeWork_Click_Upload_Success_Know_Button()
    #     # 断言 作业提交状态
    #     assert cases["status"] == homework_page.HomeWork_Get_Task_Status()

    @pytest.mark.parametrize("cases", ClassParty_HomeWork_Updata_Task_Data)
    def test_update_task(self,cases,ClassParty_Course_fixture):
        course_page, homework_page = ClassParty_Course_fixture
        # 点击作业已提交
        course_page.Course_Click_Subitted_Button()
        # 点击更新提交按钮
        homework_page.HomeWork_Click_Update_Submit_Button()
        # 点击更新提交提示弹框确定
        homework_page.HomeWork_Click_Update_Frame_Ok_Button()
        # 更新作业
        homework_page.HomeWork_Upload_Task(cases["files"])
        # 点击更新提交
        homework_page.HomeWork_Click_Updated_Submit()
        # 断言
        assert cases["Expect"] == homework_page.HomeWork_Get_Upload_Success_Text()
        # 点击我知道了
        homework_page.HomeWork_Click_Upload_Success_Know_Button()
        # 断言 作业提交状态
        assert cases["status"] == homework_page.HomeWork_Get_Task_Status()


