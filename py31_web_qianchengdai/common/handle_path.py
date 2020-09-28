import os

# 获取根目录
BASE_URL =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# commom 目录
COMMOM_DIR = os.path.join(BASE_URL,"common")
# conf 目录
C0NF_DIR = os.path.join(BASE_URL,"conf")
# data目录
DATA_DIR = os.path.join(BASE_URL,'data')
# locator 目录
LOCATOR_DIR =os.path.join(BASE_URL,'locator')
# logs 目录
LOGS_DIR = os.path.join(BASE_URL,'logs')
# pages 目录
PAGES_DIR = os.path.join(BASE_URL,'pages')
# reports 目录
REPORTS_DIR = os.path.join(BASE_URL,'reports')
# testcase 目录
TESTCASE_DIR = os.path.join(BASE_URL,'testcase')

