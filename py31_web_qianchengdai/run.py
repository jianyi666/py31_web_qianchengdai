import pytest
import os
pytest.main(["-m","classparty","--alluredir=test_result/future/reports"])
os.system('allure serve test_result/future/reports')