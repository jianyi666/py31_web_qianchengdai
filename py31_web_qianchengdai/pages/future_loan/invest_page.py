#_*_coding:utf-8 -*-
#@Time     :2020/10/1520:12
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :invest_page.py
#@Sotfware :PyCharm
from common.base_page import BasePage
from locator.future_loan.locators import Invest
import time
class InvestPage(BasePage):

    def input_invest_amount(self,amount):
        """
        输入投资金额
        :param amount:
        :return:
        """
        self.input_ele_sendkeys(Invest.invest_input_box,amount,"投资金额输入框")

    def click_invest_button(self):
        """
        点击投标按钮
        :return:
        """
        time.sleep(1)
        self.click_ele(Invest.invest_button_invest,"点击投标按钮")

    def get_invest_button_text(self):
        """
        获取投标按钮上提示文本
        :return:
        """
        return self.get_ele_text(Invest.invest_button_invest,"获取投标按钮上的提示文本")
    def get_error_box_text(self):
        """
        获取错误弹框文本
        :return:
        """
        self.wait_ele_visibility(Invest.invest_error_box_text, "等待提示弹框内的文本可见")
        return self.get_ele_text(Invest.invest_error_box_text,"获取提示弹框内的文本信息")

    def get_invest_success_box_text(self):
        """
        获取投资成功，提示弹框信息
        :return:
        """
        time.sleep(1)
        return self.get_ele_text(Invest.invesr_success_box_text,"获取投标成功提示框内的文本信息")
    def get_invest_input_balance(self):
        """
        获取投资输入框用户余额
        :return:
        """
        return self.get_ele_attribute(Invest.invest_input_box,"data-amount","获取投资输入框的内余额")

    def click_view_and_activate(self):
        """
        点击查看并激活
        :return:
        """
        time.sleep(1)
        self.click_ele(Invest.invest_view_and_activate,"点击查看并激活")

    def click_box_determine(self):
        """
        点击提示框中的确定
        :return:
        """
        self.click_ele(Invest.invest_box_determine,"点击提示框中的确认")
