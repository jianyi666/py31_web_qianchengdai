#_*_coding:utf-8 -*-
#@Time     :2020/10/2521:31
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :class_party_index_data.py
#@Sotfware :PyCharm


ClassParty_Index_Error_Data=[
    {"title":"课程代码少于6位","code":"1","Expect":"加课验证码必须是6位字符"},
    {"title":"课程代码输入错误","code":"123456","Expect":"该加课码不存在或者已经失效"},
    {"title":"课程代码大于6位","code":"12345678","Expect":"该加课码不存在或者已经失效"},
    {"title": "课程代码少于6个空格", "code": "   ", "Expect": "加课验证码必须是6位字符"},
    {"title":"课程代码大于6位空格","code":"        ","Expect":"加课码不能为空"},
    {"title": "课程代码少于6个符号", "code": "@", "Expect": "加课验证码必须是6位字符"},
    {"title":"课程代码大于6位符号","code":"@@@@@@@@@@","Expect":"该加课码不存在或者已经失效"},
]

ClassParty_Index_Success_Data=[
    {"title":"加入课程成功","code":"P69UVV","Expect":"加入课堂成功"},

]

ClassParty_Index_Repeat_Join_Data=[
    {"title": "重复加入课程", "code": "P69UVV", "Expect": "你已经选过此课程"},
]

ClassParty_Index_Into_Course_Data=[
    {"title": "进入课程", "Expect": "P69UVV"},
]

ClassParty_Index_Drop_Out_Error_Data=[
    {"title": "退课密码输入1位", "PassWord":"1","Expect": "密码错误"},
    {"title": "退课密码输入空格", "PassWord":"  ","Expect": "密码错误"},
    {"title": "退课密码输入错误密码", "PassWord":"1234567","Expect": "密码错误"},
]

ClassParty_Index_Drop_Out_Success_Data=[
    {"title": "退课密码输入1位", "PassWord":"123456a","Expect": "课程退课成功"},
]
