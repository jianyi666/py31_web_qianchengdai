#_*_coding:utf-8 -*-
#@Time     :2020/10/1520:13
#@Author   :31-北京-健壹
#@微信      :411758135
#@File     :invest_data.py
#@Sotfware :PyCharm

invest_success_data=[
    {"title":"投标成功","amount":10000,"expected":"投标成功！"},
]
invest_error_info_data=[
    {"title":"输入非10的倍数","amount":11,"expected":"请输入10的整数倍"},
    {"title":"输入小数","amount":11.33,"expected":"请输入10的整数倍"},
    {"title":"输入非数字","amount":"aaa","expected":"请输入10的整数倍"},

]

invest_error_windows_data=[
    {"title":"输入0","amount":0,"expected":"请正确填写投标金额"},
    {"title":"输入负数","amount":-1000,"expected":"请正确填写投标金额"},
    {"title":"投标金额大于可用金额","amount":1000000000000,"expected":"投标金额大于可用金额"},
    {"title":"小于最小起投金额","amount":10,"expected":"投标金额必须为100的倍数"},
]