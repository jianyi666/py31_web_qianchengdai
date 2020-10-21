#_*_coding:utf-8 -*-
#@Time     :2020/9/2722:34
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_login_case.py
#@Sotfware :PyCharm
from data.future_loan.login_data import login_data
import pytest

@pytest.mark.parametrize("cases",login_data)
class Test_Login():
    def test_login(self,cases,Login_SetUp):
        login_page,index_page = Login_SetUp
        # 登录输入账号密码进行登录
        login_page.login(cases["phone"],cases["pwd"])
        if cases['title'] == "登陆成功":
            res = index_page.get_my_account_ele()
            assert res
            index_page.get_out()
            index_page.get_in()
        elif "为空" in cases['title']:
            none_ele_text = login_page.get_page_error_info()
            assert cases['expected'] == none_ele_text
        elif "错误" in cases['title'] or "未授权" in cases['title']:
            error_ele_text = login_page.get_toast_error_info()
            assert cases["expected"] == error_ele_text
