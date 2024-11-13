"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""
import requests


class SendMessageToWeCom():
    def __init__(self, total, passed, failed, error, skipped):
        self.url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx-xxx-xxx-xxx-4cxxxxx89'
        self.header = {'Content-Type': 'applocation/json'}
        message = '自动化已完成，总共{}条，通过<font color=\"info\">{}条</font>,失败<font color=\"warning\">{}条</font>,error<font color="red">{}条</font>,skipped<font color="blue">{}条</font>'.format(total, passed, failed, error, skipped)
        self.payload = {
            "msgtype": "markdown",
            "markdown": {
                "content": message,
            }
        }
        self.remind = {
            "msgtype": "text",
            "text": {
                "mentioned_list": ["zhupeipei@sailvan.com", ""],
                "mentioned_mobile_list": ["15608401928", ""]
            }
        }


    def sendMessageWeCom(self):
        requests.post(url=self.url, headers=self.header, json=self.payload)
        requests.post(url=self.url, headers=self.header, json=self.remind)