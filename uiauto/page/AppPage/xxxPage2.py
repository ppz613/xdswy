"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import time

from selenium.webdriver.common.by import By

from common.common_fun import Common


class TroubleshootingPage(Common):
    # troubleshooting元素
    loc_troubleshooting_id = (By.ID, 'van-tabs-1-0')
    # 指导视频元素
    loc_videoGuides_id = (By.ID, 'van-tabs-1-1')
    # EBike说明书元素
    loc_EBikeManuals_id = (By.ID, 'van-tabs-1-2')
    # FAQ元素
    loc_FAQ_css = (By.CSS_SELECTOR, '#van-tab-2 > div.tabs > div.tab.active > div.text.active')
    # 重要组成部件元素
    loc_ImportantComponents_css = (By.CSS_SELECTOR, '#van-tab-2 > div.tabs > div.tab.active > div.text.active')
    # 错误码元素
    loc_Code_css = (By.CSS_SELECTOR, '#van-tab-2 > div.tabs > div.tab.active > div.text.active')

    # 先切换到webview页面，再进入指导视频页面
    def enterVideoGuides(self):
        # 切换到webview页面
        self.getTargetContext(i=1)
        # 进入指导视频页面
        self.click(self.loc_videoGuides_id)

    # 先切换到webview页面，再进入车辆说明书页面
    def enterEbikeManuals(self):
        # 切换到webview页面
        self.getTargetContext(i=1)
        # 进入车辆说明书页面
        self.click(self.loc_EBikeManuals_id)

    # 先切换到webview页面，再进入自检手册页面
    def enterTroubleshooting(self):
        # 切换到webview页面
        self.getTargetContext(i=1)
        # 进入自检手册页面
        self.click(self.enterTroubleshooting())

    # 切换到自检手册_重要部件
    def enterImportantComponents(self):
        # 切换到webview页面
        self.getTargetContext(i=1)
        # 进入自检手册页面
        self.click(self.loc_troubleshooting_id)
        time.sleep(3)
        # 进入到重要部件页面
        self.click(self.loc_ImportantComponents_css)

    # 切换到自检手册_错误码
    def enterTroubleshootingCode(self):
        # 切换到webview页面
        self.getTargetContext(i=1)
        # 进入自检手册页面
        self.click(self.loc_troubleshooting_id)
        time.sleep(3)
        # 进入到错误码页面
        self.click(self.loc_Code_css)

    # 切换到自检手册_常见问答
    def enterTroubleshootingFAQ(self):
        # 切换到webview页面
        self.getTargetContext(i=1)
        # 进入自检手册页面
        self.click(self.loc_troubleshooting_id)
        time.sleep(3)
        # 进入到常见问答页面
        self.click(self.loc_Code_css)
