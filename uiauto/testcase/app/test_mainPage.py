"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import time

import allure

from common.desired_caps import appium_desired
from page.AppPage.xxxpage import LoginPage
from page.AppPage.xxxPage6 import MainPage
from page.AppPage.xxxPage4 import ResgiLogPage
from page.AppPage.xxxPage3 import StartPage


class TestMainPage():
    # 1.初始化driver进入启动页
    app_driver = None

    def setup_method(self):
        # 1.初始化driver
        TestMainPage.app_driver = appium_desired()
        # 3.进入XX页
        ResgiLogPage(TestMainPage.app_driver).enterLogin()
        # 4.成功
        LoginPage(TestMainPage.app_driver).accountLogin("xxx@gmail.com", "xxxx")
        time.sleep(3)

    # 测试xxx功能
    @allure.story('测试xxx功能')
    def test001(self):
        MainPage(TestMainPage.app_driver).selectEbike()
        # 获取文本
        text1 = app_driver.get_attribute(value='text')
        text2 = app_driver.get_attribute(value='text')
        list1 = ['xxx xx', 'xxx xx']
        # 判断 'Log In'==获取登录的文本 且 'Register Now' ==获取注册的文本
        if text1 in list1 and text2 in list1:
            print("测试通过")
        else:
            print("测试不通过")

