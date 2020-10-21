import pytest
import os
pytest.main(["--alluredir=test_result/reports"])
os.system('allure serve test_result/reports')