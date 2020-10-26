#_*_coding:utf-8 -*-
#@Time     :2020/10/2518:11
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :conftest.py
#@Sotfware :PyCharm
import pytest
import time
from common.handle_config import config
from selenium.webdriver import Chrome
from pages.class_party.class_party_login_page import ClassPartyLoginPage
from pages.class_party.class_party_index_page import ClassPartyIndexPage
from pages.class_party.class_party_course_page import ClassPartyCoursePage
from pages.class_party.class_party_homework_page import ClassPartyHomeWorkPage
from pages.class_party.class_party_private_information_page import ClassPartyPrivateInformationPage
@pytest.fixture(scope='class')
def ClassParty_Login_fixture():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get(config.get("class_party","BASE_URL"))
    driver.maximize_window()
    login_page = ClassPartyLoginPage(driver)
    # Login 页面关闭弹框
    login_page.Login_Close_Frame()
    # Login页面点击登录
    login_page.Login_Click_Login()
    index_page = ClassPartyIndexPage(driver)
    yield login_page,index_page
    driver.quit()

@pytest.fixture(scope="class")
def ClassParty_Index_fixture():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get(config.get("class_party", "BASE_URL"))
    driver.maximize_window()
    login_page = ClassPartyLoginPage(driver)
    login_page.Login_Close_Frame()
    login_page.Login_Click_Login()
    login_page.Login_Input_Account(config.get("ClassParty_IndexPage","Account"))
    login_page.Login_Input_PassWord(config.get("ClassParty_IndexPage","Password"))
    login_page.Login_Click_Login_Button()
    index_page = ClassPartyIndexPage(driver)
    # 点击加入课程
    index_page.Index_Click_Join_Class()
    course_page = ClassPartyCoursePage(driver)
    yield index_page,course_page
    driver.quit()

@pytest.fixture(scope='class')
def ClassParty_Course_fixture():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get(config.get("class_party", "BASE_URL"))
    driver.maximize_window()
    #Login页面，登陆
    login_page = ClassPartyLoginPage(driver)
    login_page.Login_Close_Frame()
    login_page.Login_Click_Login()
    login_page.Login_Input_Account(config.get("ClassParty_IndexPage", "Account"))
    login_page.Login_Input_PassWord(config.get("ClassParty_IndexPage", "Password"))
    login_page.Login_Click_Login_Button()
    #Index页面，加入课程
    index_page = ClassPartyIndexPage(driver)
    index_page.Index_Click_Join_Class()
    index_page.Index_Input_Class_Code(config.get("ClassParty_CoursePage","CourseCode"))
    index_page.Index_Click_Frame_Join()
    #Index页面，进入课程，切换到作业
    index_page.Index_Click_Into_Class()
    course_page=ClassPartyCoursePage(driver)
    course_page.Course_Click_th_Task()
    homework_page = ClassPartyHomeWorkPage(driver)
    yield course_page,homework_page
    # 点击返回Course页面
    homework_page.HomeWork_Click_Back_Course()
    # 点击返回Index页面
    course_page.Course_Click_Back_Index()
    # 点击课程中的更多
    index_page.Index_Click_Class_More()
    # 点击退课
    index_page.Index_Click_Class_Quit()
    # 输入密码
    index_page.Index_Class_Frame_Input_PassWord(config.get("ClassParty_IndexPage","Password"))
    # 点击退课
    index_page.Index_Click_Class_Frame_Quit()
    time.sleep(4)
    driver.quit()

@pytest.fixture(scope='class')
def ClassParty_PrivateInformation():
    driver = Chrome()
    driver.implicitly_wait(30)
    driver.get(config.get("class_party", "BASE_URL"))
    driver.maximize_window()
    # Login页面，登陆
    login_page = ClassPartyLoginPage(driver)
    login_page.Login_Close_Frame()
    login_page.Login_Click_Login()
    login_page.Login_Input_Account(config.get("ClassParty_IndexPage", "Account"))
    login_page.Login_Input_PassWord(config.get("ClassParty_IndexPage", "Password"))
    login_page.Login_Click_Login_Button()
    # 进入私信页面
    privateinformation_page =ClassPartyPrivateInformationPage(driver)
    privateinformation_page.PrivateInformation_Click_Icon()
    yield privateinformation_page
    driver.quit()

