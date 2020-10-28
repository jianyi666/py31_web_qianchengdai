import os

# 获取根目录
BASE_URL =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# commom 目录
COMMOM_DIR = os.path.join(BASE_URL,"common")
# conf 目录
C0NF_DIR = os.path.join(BASE_URL,"conf")
# data目录
FUTURE_LOAN_DATA_DIR = os.path.join(BASE_URL,'data/future_loan')
# locator 目录
FUTURE_LOAN_LOCATOR_DIR =os.path.join(BASE_URL,'locator/future_loan')
# logs 目录
FUTURE_LOAN_LOGS_DIR = os.path.join(BASE_URL,'test_result/logs')
# pages 目录
FUTURE_LOAN_PAGES_DIR = os.path.join(BASE_URL,'pages/future_loan')
# testcase 目录
FUTURE_LOAN_TESTCASE_DIR = os.path.join(BASE_URL,'testcase/future_loan')
# ERROR_IMAGES 目录
FUTURE_LOAN_ERROR_IMAGES_DIR = os.path.join(BASE_URL,'test_result/future_loan/error_images')
# REPORTS 目录
FUTURE_LOAN_REPORTS_DIR = os.path.join(BASE_URL,'test_result/future_loan/reports')

