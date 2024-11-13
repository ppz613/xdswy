"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
from appium import webdriver as app_webdriver
from selenium import webdriver


# APP工具
def appium_desired():
    desired_caps = {}

    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['deviceName'] = '127.0.0.1:16384'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '12'
    # desired_caps['deviceName'] = 'emulator-5554'
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '9'
    desired_caps['appPackage'] = 'com.netease.newsreader.activity'
    desired_caps['appActivity'] = 'com.netease.nr.phone.main.MainActivity'
    desired_caps['adbPort'] = '5037'
    desired_caps['uiautomator2ServerLaunchTimeout'] = '60000'
    desired_caps['noReset'] = False
    desired_caps['newCommandTimeout'] = 600
    desired_caps['chromedriverExecutable'] = r'D:\ChromeDriver\2.9\chromedriver.exe'
    driver = app_webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    return driver


def quit_appDriver():
    appium_desired().close()


# web工具
def selenium_desired():
    driver = webdriver.Chrome()
    driver.get('http://xxx-xxx-xxx.xxx.xxx:9010/xxx/admin/login')