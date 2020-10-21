#_*_coding:utf-8 -*-
#@Time     :2020/10/1520:14
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_invest_case.py
#@Sotfware :PyCharm
import pytest
from data.future_loan.invest_data import invest_success_data,invest_error_info_data,invest_error_windows_data


class Test_Invest():


    @pytest.mark.parametrize("cases",invest_error_info_data)
    def test_invest_error_info_button(self,cases,Invest_SetUp):
        """
        投标失败，button错误提示
        :param Invest_SetUp:
        :return:
        """
        #从conftest中获取invest_page
        invest_page = Invest_SetUp[0]
        #输入投资金额
        invest_page.input_invest_amount(cases["amount"])
        # 获取投标按钮提示文本
        res=invest_page.get_invest_button_text()
        # 断言
        assert cases["expected"] == res

    @pytest.mark.parametrize("cases",invest_error_windows_data)
    def test_invest_error_windows_button(self, cases, Invest_SetUp):
        """
        投标失败，button错误提示
        :param Invest_SetUp:
        :return:
        """
        # 从conftest中获取invest_page
        invest_page = Invest_SetUp[0]
        # 输入投资金额
        invest_page.input_invest_amount(cases["amount"])
        # 点击投标按钮
        invest_page.click_invest_button()
        # 获取弹框提示文本
        res =invest_page.get_error_box_text()
        # 断言
        assert cases["expected"] == res
        invest_page.click_box_determine()

    @pytest.mark.parametrize("cases", invest_success_data)
    def test_invest_success(self, cases, Invest_SetUp):
        """
        投资成功
        :param cases:
        :param Invest_SetUp:
        :return:
        """
        # 从conftest中获取 invest_page user_page
        invest_page, user_page = Invest_SetUp
        # 获取用户可用余额
        i_balance = invest_page.get_invest_input_balance()
        # 输入投标金额
        invest_page.input_invest_amount(cases["amount"])
        # 点击投标按钮
        invest_page.click_invest_button()
        # 获取投标成功弹框文案
        success_text = invest_page.get_invest_success_box_text()
        # 断言预期结果与实际提示结果
        assert cases["expected"] == success_text
        # 点击查看并激活
        invest_page.click_view_and_activate()
        # 获取用户页面可用余额
        u_balance = user_page.get_user_available_balance()
        # 断言投资金额
        assert float(i_balance) - float(u_balance) == cases["amount"]