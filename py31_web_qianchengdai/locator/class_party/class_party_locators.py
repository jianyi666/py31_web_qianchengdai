#_*_coding:utf-8 -*-
#@Time     :2020/10/2120:57
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_locators.py
#@Sotfware :PyCharm
from selenium.webdriver.common.by import By

class ClassParty_Login():
    Login_Login =(By.XPATH,"//div[@id='indextop']//a[@class='login']")
    Login_Frame_Close = (By.XPATH,"//div[@id='layui-layer1']//a[@class='layui-layer-ico layui-layer-close layui-layer-close2']")
    Login_Get_Into_Class=(By.XPATH,"//div[@class='jr-ktp']//span")
    Login_Input_Account=(By.XPATH,"//div[@class='padding-cont pt-login']//input[@name='account']")
    Login_Input_PassWord=(By.XPATH,"//div[@class='padding-cont pt-login']//input[@name='pass']")
    Login_Login_Button =(By.XPATH,"//div[@class='padding-cont pt-login']//a[text()='登录']")
    Login_Error_Tips=(By.XPATH,"//div[@class='padding-cont pt-login']//p[@class='error-tips']")


class ClassParty_Index():
    Index_Join_Course_Error_Tips=(By.XPATH,"//div[@id='error-tip']/span")
    Index_user =(By.XPATH,"//a[@id='user']")
    Index_Join_Course = (By.XPATH,"//div[@class='ktcon1l fr']")
    Index_Frame_Input_class_code=(By.XPATH,"//div[@class='chuangjiankccon']/input")
    Index_Frame_Cancel=(By.XPATH,"//div[@class='chuangjiankcbot']//a[@class='btn btn-defalut']")
    Index_Frame_Join=(By.XPATH,"//div[@class='chuangjiankcbot']//a[@class='btn btn-positive']")
    Index_Into_Class=(By.XPATH,"//dl[@data-id='MDAwMDAwMDAwMLR2vd6Gz8mw']//a[text()='python-web项目实战- 考核项目']")
    Index_Class_More=(By.XPATH,"//dl[@data-id='MDAwMDAwMDAwMLR2vd6Gz8mw']//span[text()='更多']")
    Index_Class_Quit=(By.XPATH,"//dl[@data-id='MDAwMDAwMDAwMLR2vd6Gz8mw']//a[text()='退课']")
    Index_Frame_Login_PassWord=(By.XPATH,"//div[@class='deletekt']//input")
    Index_Class_Frame_Quit=(By.XPATH,"//div[@class='deletekt']//a[text()='退课']")
    Index_Class_Frame_Cancel=(By.XPATH,"//div[@class='deletekt']//a[text()='取消']")
    Index_Toast_PassWord_Error =(By.XPATH,"//div[@id='error-tip']/span")
    Index_Toast_Join_And_Drop_Class_Success = (By.XPATH,"//div[@id='show-tip']/span")

class ClassParty_Course():
    Course_Back_Index =(By.XPATH,"//div[@class='nav nav-clear clearfix course-nav']//a[text()='课堂 ']")
    Course_Code=(By.XPATH,"(//div[@class='codetip'])[3]")
    Course_Task=(By.XPATH,"//div[@id='third-nav']/a[text()='作业']")
    Course_Upload_task=(By.XPATH,"//div[@class='announce-cont-box']//a[text()='上传作业']")
    Course_Submitted_Button=(By.XPATH,"//div[@class='announce-cont clearfix']//a[text()='已提交']")
    Course_Task_Name=(By.XPATH,"//div[@class='work-new-l fl']//a")


class ClassParty_HomeWork():
    HomeWork_Back_Course = (By.XPATH,"//a[@id='return-course']//span")
    HomeWork_Leave_Message =(By.XPATH,"//div[@id='mess1']/span[@class='s1']")
    HomeWork_Input_Leave_Message =(By.XPATH,"//div[@class='work-message2 clearfix']/textarea")
    HomeWork_Kept_Levae_Message=(By.XPATH,"//div[@class='work-message2 clearfix']/a")
    HomeWork_Add_task = (By.XPATH, "//a[@class='sc-btn webuploader-container']")
    HomeWork_Upload = (By.XPATH, "//div[@class='sc-tj-box']//a[text()='提交']")
    HomeWork_System_Prompt_submit_success = (By.XPATH, "//div[@class='weui_dialog']//div[@class='weui_dialog_bd']")
    HomeWork_System_Prompt_Know = (By.XPATH, "//div[@class='weui_dialog']//a[text()='知道了']")
    HomeWorK_Task_Upload_Status= (By.XPATH,"//div[@class='status fr']/span")
    HomeWork_Task_Discuss =(By.XPATH,"//div[@id='third-nav']/a[text()='作业讨论']")
    HomeWork_Add_comments =(By.XPATH,"//div[@class='input fr']/textarea")
    HomeWork_Confirm = (By.XPATH,"//div[@class='opt-btn fr']/a[text()='确定']")
    HomeWork_Cancel = (By.XPATH,"//div[@class='opt-btn fr']/a[text()='取消']")
    HomeWork_View_Task_Status=(By.XPATH,"//div[@class='status fr']/span")
    HomeWork_Update_Submit_Button=(By.XPATH,"//div[@class='sc-tj fl']/a[@class='new-tj1']")
    HomeWork_Updated_Submit_Button =(By.XPATH,"//div[@class='sc-tj fl']/a[@class='new-tj2 active']")
    HomeWork_Update_Work_Frame_OK_Button=(By.XPATH,"//div[@id='update-pop']//a[text()='确定']")
    HomeWork_Update_Work_Frame_Cancel_Button=(By.XPATH,"//div[@id='update-pop']//a[text()='取消']")
    HomeWork_Delete_Work=(By.XPATH,"//div[@class='opt clearfix']//a[text()='删除']")


class ClassParty_PrivateInformation():

    PrivateInformation_Icon=(By.XPATH,"//div[@class='privateLetter']/a")
    PrivateInformation_Contacts=(By.CSS_SELECTOR,"#chat a[class=classp]")
    PrivateInformation_Py31=(By.XPATH,"//h2[@title='python自动化第31期']")
    PrivateInformation_Choice_Contact=(By.XPATH,"//ul[@class='re-ul']/li/p[text()='柠檬班--丹丹']")
    PrivateInformation_Input_Text=(By.XPATH,"//div[@class='m-text']/textarea")
    PrivateInformation_Send_Out=(By.XPATH,"//div[@class='m-text']//a[text()='发送']")