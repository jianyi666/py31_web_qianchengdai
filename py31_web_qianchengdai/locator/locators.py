#_*_coding:utf-8 -*-
#@Time     :2020/9/2722:05
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :locators.py
#@Sotfware :PyCharm
from selenium.webdriver.common.by import  By

class Login():
    login_mobile_locator = (By.XPATH,"//input[@name='phone']")
    login_pwd_locator =  (By.XPATH,"//input[@name='password']")
    login_button_locator = (By.XPATH,"//button[@class='btn btn-special']")
    login_page_error_locator = (By.XPATH,"//div[@class ='form-error-info']")
    login_toast_error_locator = (By.XPATH,"//div[@class ='layui-layer-content']")

class Index():
    index_my_account_locator = (By.XPATH,"//a[contains(text(),'我的帐户')]")
    index_get_out_locator = (By.XPATH,"//span/a[text()='退出']")
    index_get_in_locator = (By.XPATH,"//span/a[text()='登录']")
    index_rush_to_bid = (By.XPATH,"(//div[@class='text-center'])[1]/a")

class Invest():

    invest_input_box = (By.XPATH,"//div[@class='clearfix left']/input")
    invest_button_invest =(By.XPATH,"//div[@class='pd-right']/button")
    invest_error_box_text = (By.XPATH,"//div[@id='layui-layer4']//div[@class='text-center']")
    invesr_success_box_text = (By.XPATH,"(//div[@class='capital_ts'])[2]//div[@class='capital_font1 note']")
    invest_view_and_activate =(By.XPATH,"//div[@class='layui-layer-content']//button")

class User():
    pass