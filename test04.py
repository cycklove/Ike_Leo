#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import requests, sys
import datetime


class SendWeiXinWork():
    def __init__(self):
        self.CORP_ID = "ww777831676749db7f"  # 企业号的标识
        self.SECRET = "kkjfvIBkA4d2Qd3UJhImKSNEiUnqr7wxpToZCI8jTcc"  # 管理组凭证密钥
        self.AGENT_ID = 1000002  # 应用ID
        self.token = self.get_token()

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {
            "corpid": self.CORP_ID,
            "corpsecret": self.SECRET
        }
        req = requests.get(url=url, params=data)
        res = req.json()
        if res['errmsg'] == 'ok':
            return res["access_token"]
        else:
            return res

    def send_message(self, to_user, content):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % self.token
        data = {
            #"touser": "ChenBan",  # 发送个人就填用户账号
            "toparty": 2,  # 发送组内成员就填部门ID
            "msgtype": "text",
            "agentid": self.AGENT_ID,
            "text": {"content": content},
            "safe": "0"
        }

        req = requests.post(url=url, json=data)
        res = req.json()
        if res['errmsg'] == 'ok':
            print("send message sucessed")
            return "send message sucessed"
        else:
            return res

def testsj():
    i = 0
    a = datetime.datetime.now()
    while i < 10000000:
        i+=1
        # print(i)
    b = datetime.datetime.now()
    print("运行时间：" + str(b - a) + " 秒")

if __name__ == '__main__':
    SendWeiXinWork = SendWeiXinWork()
    SendWeiXinWork.send_message("2", "测试a")
    testsj()