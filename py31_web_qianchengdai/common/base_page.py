#_*_coding:utf-8 -*-
#@Time     :2020/10/1521:51
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :base_page.py
#@Sotfware :PyCharm
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver import Chrome
from common.handle_logs import log
from common.handle_path import FUTURE_LOAN_ERROR_IMAGES_DIR
import  time
class BasePage():

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def error_screenshot(self,filename):
        """
        截图操作
        :param filename:
        :return:
        """
        data_desc = time.strftime("%y-%m-%d_%H_%M_%S")
        filepath = FUTURE_LOAN_ERROR_IMAGES_DIR +"\\"+ data_desc +'_'+filename+'.png'
        self.driver.save_screenshot(filepath)

    def wait_ele_visibility(self,locator,locator_desc):
        """
        等待元素被加载
        :param locator:
        :param locator_desc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"等待元素-【{locator_desc}】-可见失败！")
            log.exception(e)
        else:
            log.info(f"等待元素-【{locator_desc}】-可见成功！")

    def wait_ele_clickable(self,locator,locator_desc):
        """
        等待元素可点击
        :param locator:
        :param locator_desc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"等待元素-【{locator_desc}】-可点击失败！")
            log.exception(e)
        else:
            log.info(f"等待元素-【{locator_desc}】-可点击成功！")

    def wait_ele_presence(self,locator,locator_desc):
        """
        等待元素可见
        :param locator:
        :param locator_desc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"等待元素-【{locator_desc}】-被加载失败！")
            log.exception(e)
        else:
            log.info(f"等待元素-【{locator_desc}】-被加载成功！")

    def find_ele(self,locator,locator_desc):
        """
        查找元素
        :param locator:
        :param locator_desc:
        :return:
        """
        try:
            self.driver.find_element(*locator)
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"查找元素-【{locator_desc}】-失败！")
            log.exception(e)
            raise e
        else:
            log.info(f"查找元素-【{locator_desc}】-成功！")

    def click_ele(self,locator,locator_desc):
        """
        点击元素
        :param locator:
        :param locator_desc:
        :return:
        """
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"点击元素-【{locator_desc}】-失败！")
            log.exception(e)
            raise e
        else:
            log.info(f"点击元素-【{locator_desc}】-成功！")

    def input_ele_sendkeys(self,locator,value,locator_desc):
        """
        send_keys
        :param locator:
        :param value:
        :param locator_desc:
        :return:
        """
        try:
            self.driver.find_element(*locator).clear()
            self.driver.find_element(*locator).send_keys(value)
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"向元素-【{locator_desc}】-发送内容失败！")
            log.exception(e)
        else:
            log.info(f"向元素-【{locator_desc}】-发送内容成功！")

    def get_ele_text(self,locator,locator_desc):
        """
        获取元素中的文本信息
        :param locator:
        :param locator_desc:
        :return:
        """
        try:
            res = self.driver.find_element(*locator).text
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"获取元素-【{locator_desc}】-文本内容失败！")
            log.exception(e)
        else:
            log.info(f"获取元素-【{locator_desc}】-文本内容成功！")
            return res

    def get_ele_attribute(self,locator,attribute,locator_desc):
        """
        获取元素的属性
        :param locator:
        :param attribute:
        :param locator_desc:
        :return:
        """
        try:

            res = self.driver.find_element(*locator).get_attribute(attribute)
        except Exception as e:
            self.error_screenshot(locator_desc)
            log.error(f"查找元素-【{locator_desc}】-的【{attribute}】属性失败！")
            log.exception(e)
        else:
            log.info(f"查找元素-【{locator_desc}】-的【{attribute}】属性成功！")
            return res

if __name__ == '__main__':
    dirver = Chrome()
    dirver.get("https://www.baidu.com/")
    bp = BasePage(dirver)
    bp.error_screenshot("baidu")
    dirver.quit()