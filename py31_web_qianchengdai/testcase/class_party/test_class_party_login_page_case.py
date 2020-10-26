#_*_coding:utf-8 -*-
#@Time     :2020/10/2518:10
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_class_party_login_page_case.py
#@Sotfware :PyCharm
import pytest
import time
from data.class_party.class_party_login_data import Class_Party_Login_error,Class_Party_Login_success
class Test_ClassParty_Login():
    pytestmark = [pytest.mark.classparty]
    @pytest.mark.parametrize("cases",Class_Party_Login_error)
    def test_login_error_info(self,ClassParty_Login_fixture,cases):
        login_page,index_page = ClassParty_Login_fixture
        # Login页面输入账号
        login_page.Login_Input_Account(cases["Account"])
        # Login页面输入密码
        login_page.Login_Input_PassWord(cases["PassWord"])
        # Login页面点击登录
        login_page.Login_Click_Login_Button()
        # 断言
        assert cases["Expect"] == login_page.Login_Get_Login_Error_Text()

    @pytest.mark.parametrize("cases",Class_Party_Login_success)
    def test_login_success(self,cases,ClassParty_Login_fixture):
        login_page, index_page = ClassParty_Login_fixture
        login_page, index_page = ClassParty_Login_fixture
        # Login页面输入账号
        login_page.Login_Input_Account(cases["Account"])
        # Login页面输入密码
        login_page.Login_Input_PassWord(cases["PassWord"])
        # Login页面点击登录
        login_page.Login_Click_Login_Button()
        # Index页面检查登录成功
        # 断言
        assert cases["Expect"] == index_page.Index_Find_Login_User()
