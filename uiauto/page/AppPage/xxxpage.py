"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import time

# from basePage.common_fun import Common
from selenium.webdriver.common.by import By

from common.common_fun import Common


class LoginPage(Common):

    loc_email_path = (By.XPATH, "//*[@text='Email']")
    loc_pwd_id = (By.ID, 'xxx.xxx.xxx.xxx:id/et_password')
    loc_box_id = (By.ID, 'xxx.xxx.xxx.xxx:id/box_agreement')
    loc_login01_id = (By.ID, 'xxx.xxx.xxx.xxx:id/btn_sign')

    # 登录
    def accountLogin(self, email, password):
        # 输入邮箱号
        self.click(self.loc_email_path)
        self.input(self.loc_email_path, email)
        time.sleep(5)
        # 输入密码
        self.click(self.loc_pwd_id)
        self.input(self.loc_pwd_id, password)
        # 收起键盘
        self.hideKeybord()
        # 勾选协议
        self.click(self.loc_box_id)
        # 点击登录
        self.click(self.loc_login01_id)
        time.sleep(3)
        # 处理系统弹窗
        for i in range(3):
            self.clickByTap()
        time.sleep(3)

