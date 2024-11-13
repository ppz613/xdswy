"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
# from basePage.common_fun import Common
from selenium.webdriver.common.by import By

from common.common_fun import Common


class ResgiLogPage(Common):

    # 测试
    loc_login_id = (By.ID, 'xxx.xxx.xxx.xxx:id/bt_sign')
    loc_resgi_id = (By.ID, 'xxx.xxx.xxx.xxx:id/bt_register')

    # 进入登录页面
    def enterLogin(self):
        self.click(self.loc_login_id)
        # self.clickById(self.login_id)

    # 进入注册页面
    def enterResgi(self):
        self.click(self.loc_resgi_id)