"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
from selenium.webdriver.support.wait import WebDriverWait

# from common.desired_caps import appium_desired


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, loc, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))
            return ele
        except Exception as e:
            print(f"未找到指定的元素，抛出异常为{e}")

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 获取元素属性中的text值
    def getEleText(self, loc):
        ele_text = self.locator(loc).text
        return ele_text

    # 切换到native APP
    def getTargetContext(self, i=0):
        # 如果i为0，切换到native APP；如果i为1切换到webview
        if i == 0:
            targetContext = self.driver.contexts[0]
        elif i == 1:
            targetContext = self.driver.contexts[-1]
        return targetContext


