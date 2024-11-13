"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import time

from selenium.webdriver.common.by import By

from common.common_fun import Common


class MainPage(Common):
    # 首页骑行记录
    loc_rideHistory_id = (By.ID, 'xxx.xxx.xxx.xxx:id/iv_history')
    # 首页GO
    loc_go_id = (By.ID, 'xxx.xxx.xxx.xxx:id/iv_go')
    # 首页社区
    loc_issue_id = (By.ID, 'xxx.xxx.xxx.xxx:id/iv_issue')
    # 首页我的
    loc_me_id = (By.ID, 'xxx.xxx.xxx.xxx:id/iv_me')
    # 首页车辆下拉框
    loc_selectEbike_id = (By.ID, 'xxx.xxx.xxx.xxx:id/tv_name')
    # 首页目标车辆
    loc_targetEbike_xpath = (By.XPATH, '//*[@text="MyEBike03(5e47)"]')
    # 首页消息中心
    loc_notice_id = (By.ID, 'xxx.xxx.xxx.xxx:id/iv_notify')
    # 首页导航
    loc_navigation_xpath = (By.XPATH, '//*[@text="Navigation"]')
    # 首页设置
    loc_setting_xpath = (By.XPATH, '//*[@text="Setting"]')

    @classmethod
    def enterRideHistoryPage1(cls):
        cls.click(loc=cls.loc_rideHistory_id)

    # 从首页切换到骑行记录
    def enterRideHistoryPage(self):
        self.click(self.loc_rideHistory_id)

    # 从首页切换到GO
    def enterGOPage(self):
        self.click(self.loc_go_id)

    # 从首页切换到社区
    def enterIssuePage(self):
        self.click(self.loc_issue_id)

    # 从首页切换到我的
    def enterMePage(self):
        self.click(self.loc_me_id)

    # 从首页切换车辆
    def selectEbike(self):
        self.click(self.loc_selectEbike_id)
        time.sleep(1)
        self.click(self.loc_targetEbike_xpath)

    # 从首页进入消息中心
    def enterInbox(self):
        self.click(self.loc_notice_id)

    # 从首页进入导航
    def enterMap(self):
        self.click(self.loc_navigation_xpath)

    # 从首页进入设置
    def enterSetting(self):
        self.click(self.loc_setting_xpath)

    # 从首页进入排行榜
    def enterBank(self):
        pass