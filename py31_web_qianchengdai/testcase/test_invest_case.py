#_*_coding:utf-8 -*-
#@Time     :2020/10/1520:14
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :test_invest_case.py
#@Sotfware :PyCharm
import pytest
from data.invest_data import invest_data

@pytest.mark.parametrize("cases",invest_data)
class Test_Invest():

    def test_invest(self,cases,Invest_SetUp):
        invest_page = Invest_SetUp
        # 输入投标金额
        invest_page.input_invest_amount(10000)
        # 点击投标按钮
        invest_page.click_invest_button()
        