"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
# from basePage.common_fun import Common
from selenium.webdriver.common.by import By

from common.common_fun import Common


class StartPage(Common):

    # 测试
    loc_next_id = (By.ID, 'xxx.xxx.xxx.xxx:id/btn_next')

    # 进入注册登录页面
    def enterRegistLogin(self):
        self.swipeLeft(3)
        self.click(self.loc_next_id)
        # self.clickById(self.next_id)
