"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir', 'result/allure-result', '--clean-alluredir'])
    os.system(r"allure generate --clean result/allure-result -o result/allure-report")