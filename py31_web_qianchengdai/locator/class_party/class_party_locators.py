#_*_coding:utf-8 -*-
#@Time     :2020/10/2120:57
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_locators.py
#@Sotfware :PyCharm
from selenium.webdriver.common.by import By

class ClassParty_Index():
    Index_Login =(By.XPATH,"//div[@id='indextop']//a[@class='login']")
    Index_Frame_Close = (By.XPATH,"//div[@id='layui-layer1']//a[@class='layui-layer-ico layui-layer-close layui-layer-close2']")
    Index_Get_Into_Class=(By.XPATH,"//div[@class='jr-ktp']//span")

class ClassParty_Room():
    Room_Join_Course = (By.XPATH,"//div[@class='ktcon1l fr']")
    Room_Frame_Input_class_code=(By.XPATH,"//div[@class='chuangjiankccon']/input")
    Room_Frame_Cancel=(By.XPATH,"//div[@class='chuangjiankcbot']//a[@class='btn btn-defalut']")
    Room_Frame_Join=(By.XPATH,"//div[@class='chuangjiankcbot']//a[@class='btn disable']")
    Room_Into_Class=(By.XPATH,"//dt[@class='bgclass1']//a[text()='python-web项目实战- 考核项目']")
    Room_Class_More=(By.XPATH,"//dt[@class='bgclass1']//span[text()='更多']")
    Room_Class_Quit=(By.XPATH,"//dt[@class='bgclass1']//a[text()='退课']")
    Room_Frame_Login_PassWord=(By.XPATH,"//div[@class='deletekt']//input")
    Room_Class_Frame_Quit=(By.XPATH,"//div[@class='deletekt']//a[text()='退课']")
    Room_Class_Frame_Cancel=(By.XPATH,"//div[@class='deletekt']//a[text()='取消']")

class ClassParty_Course():
    Course_task=(By.XPATH,"//div[@id='third-nav']/a[text()='作业']")
    Course_Upload_task=(By.XPATH,"//div[@class='announce-cont-box']//a[text()='上传作业']")


class ClassParty_HomeWork():
    HomeWork_Add_task = (By.XPATH, "//div[@class='sc-tj-box sc-tj-box-new']//div[text()='添加作业文件']")
    HomeWork_Upload = (By.XPATH, "//div[@class='sc-tj-box']//a[text()='提交']")
    HomeWork_System_Prompt_submit_success = (By.XPATH, "//div[@class='weui_dialog']//div[@class='weui_dialog_bd']")
    HomeWork_System_Prompt_Know = (By.XPATH, "//div[@class='weui_dialog']//a[text()='知道了']")
    HomeWork_Task_Discuss =(By.XPATH,"//div[@id='third-nav']/a[text()='作业讨论']")
    HomeWork_Add_comments =(By.XPATH,"//div[@class='input fr']/textarea")
    HomeWork_Confirm = (By.XPATH,"//div[@class='opt-btn fr']/a[text()='确定']")
    HomeWork_Cancel = (By.XPATH,"//div[@class='opt-btn fr']/a[text()='取消']")
    HomeWork_View_Task_Status=(By.XPATH,"//div[@class='status fr']/span")

class ClassParty_PrivateInformation():
    PrivateInformation_Icon=(By.XPATH,"//div[@class='privateLetter']/a")
    PrivateInformation_Contacts=(By.XPATH,"//div[@class='totalbar']/a[text()='联系人']")
    PrivateInformation_Py31=(By.XPATH,"//h2[@title='python自动化第31期']")
    PrivateInformation_Choice_Contact=(By.XPATH,"//ul[@class='re-ul']/li/p[text()='柠檬班--丹丹']")
    PrivateInformation_Input_Text=(By.XPATH,"//div[@class='m-text']/textarea")
    PrivateInformation_Send_Out=(By.XPATH,"//div[@class='m-text']//a[text()='发送']")