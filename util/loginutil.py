# -*- coding:utf-8 -*-
from util import unittestutil
import time
# 登录
brower=unittestutil.Chrome()
def login(self):
        # # 用户名为空，密码为空
        # self.brower.FindId("uname").clear()
        # self.brower.FindId("upwd").clear()# 密码
        # self.brower.FindClass("login-btn").click()# 登录
        # time.sleep(3)
        # self.assertEqual(self.brower.FindClass("lm-logintips-box").text, u"手机号：不能为空")
        # time.sleep(5)
        #
        # # 手机号不为空但手机号输入不正确，密码为空
        # self.brower.FindId("uname").send_keys("15111")
        # self.brower.FindId("upwd").clear()
        # self.brower.FindId("uname").click()
        # self.text1=self.brower.FindClass("lm-logintips-box").text
        # self.assertEqual(self.text1, u"手机号：请输入正确手机号")
        # time.sleep(2)
        # self.brower.FindClass("login-btn").click()
        # time.sleep(2)
        # self.text2 = self.brower.FindClass("lm-logintips-box").text
        # self.assertEqual(self.text2, u"密码：不能为空")
        # time.sleep(5)
        # #手机号输入正确，密码为空
        # self.brower.FindId("uname").send_keys("15111111111")
        # self.brower.FindId("upwd").clear()
        # self.brower.FindClass("login-btn").click()
        # time.sleep(2)
        # self.text=self.brower.FindClass("lm-logintips-box").text
        # self.assertEqual(self.text,u"密码：不能为空")
        # time.sleep(5)
        # # 手机号输入正确，密码输入不正确
        # self.brower.FindId("uname").send_keys("15111111111")
        # self.brower.FindId("upwd").send_keys(123)
        # self.brower.FindClass("login-btn").click()
        # time.sleep(2)
        # self.text = self.brower.FindClass("lm-logintips-box").text
        # self.assertEqual(self.text, u"密码：长度6-20位(数字/字母/下划线)")
        # time.sleep(5)
        # # 手机号输入正确，密码输入不正确
        # self.brower.FindId("uname").send_keys("15111111111")
        # self.brower.FindId("upwd").send_keys(1234567)
        # self.brower.FindClass("login-btn").click()
        # time.sleep(2)
        # self.text = self.brower.FindClass("lm-logintips-box").text
        # self.assertEqual(self.text, u"登录失败，密码错误")
        # time.sleep(5)
        # 手机号输入正确，密码输入正确
        self.brower.FindId("uname").send_keys("15111111111")
        self.brower.FindId("upwd").send_keys(111111)
        self.brower.FindClass("login-btn").click()
        time.sleep(3)
        self.assertEqual(self.brower.driver.title, u"个人中心")






pass

