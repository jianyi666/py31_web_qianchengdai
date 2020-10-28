import pytest
import os
pytest.main(["-m","classparty","--alluredir=test_result/class_party/reports"])
os.system('allure serve test_result/class_party/reports')