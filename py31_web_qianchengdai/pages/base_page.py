#_*_coding:utf-8 -*-
#@Time     :2020/10/1521:51
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :base_page.py
#@Sotfware :PyCharm
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from common.handle_logs import log
from common.handle_path import ERROR_IMAGES_DIR
import  time
class Base_page():

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def error_screenshot(self,filename):

        data_desc = time.strftime("%y-%m-%d_%H_%M_%S")
        filepath = ERROR_IMAGES_DIR + data_desc + filename+'.png'
        self.driver.save_screenshot(filepath)

    def wait_ele_visibility(self,locator,locator_desc):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"等待元素-【{locator_desc}】-可见失败！")
            log.exception(e)
        else:
            log.info(f"等待元素-【{locator_desc}】-可见成功！")

    def wait_ele_clickable(self,locator,locator_desc):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"等待元素-【{locator_desc}】-可点击失败！")
            log.exception(e)
        else:
            log.info(f"等待元素-【{locator_desc}】-可点击成功！")

    def wait_ele_presence(self,locator,locator_desc):
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"等待元素-【{locator_desc}】-被加载失败！")
            log.exception(e)
        else:
            log.info(f"等待元素-【{locator_desc}】-被加载成功！")

