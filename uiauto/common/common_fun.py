"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
from basePage.base_page import BasePage


class Common(BasePage):
    # 获取手机屏幕大小
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 通过坐标点击
    def clickByTap(self):
        # x = 100
        # y = 100
        self.driver.tap([(500, 500)])

    # 向左滑动
    def swipeLeft(self, n):
        lsize = self.getSize()
        x1 = lsize[0]*0.8
        x2 = lsize[0]*0.2
        y = lsize[1]*0.5
        for i in range(n):
            self.driver.swipe(x1, y, x2, y)

    # 向上滑动
    def swipeUp(self, n=1):
        usize = self.getSize()
        x = usize[0]*0.5
        y_start = usize[1]*0.8
        y_end = usize[1]*0.2
        for i in range(n):
            self.driver.swipe(x, y_start, x, y_end)

    # 通过元素滑动
    def scrollByEle(self, e_start, e_end):
        self.driver.scroll(e_start, e_end)

    # 收起键盘
    def hideKeybord(self):
        self.driver.hide_keyboard()

    # 处理系统弹窗
    def handleAler(self):
        self.driver.switch_to.alert.accept()



