"""
==================
Author:Chloeee
Time:2021/7/31 10:24
Contact:403505960@qq.com
==================
"""


import pytest

if __name__ == "__main__":
    pytest.main(["-s", "-v","--alluredir=allure-report-files","--clean-alluredir"])


# allure command line: allure server allure-report-files