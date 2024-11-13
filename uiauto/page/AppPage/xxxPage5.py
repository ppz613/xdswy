"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import time

from selenium.webdriver.common.by import By

from common.common_fun import Common


class MePage(Common):
    # 我的服务-用户支持
    loc_support_id = (By.ID, 'xxx.xxx.xxx.xxx:id/tv_support')

    # 进入用户支持页面
    def enterSupport(self):
        ele_exist = False
        # 先判断元素是否找到，找到点击，找不到向上滑动再点击
        if ele_exist:
            self.click(self.loc_support_id)
        else:
            self.swipeUp()
            time.sleep(1)
            self.click(self.loc_support_id)
        time.sleep(15)
        print("这是1", self.driver.contexts)

