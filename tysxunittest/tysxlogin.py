# -*- coding:utf-8 -*-
from util import unittestutil
from util import urlutil,loginutil
import unittest

import  time

class TYSX(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        # 实例化浏览器类的对象
        self.brower=unittestutil.Chrome()

        pass
    def setUp(self):
        # 打开浏览器
        self.brower.StartChrom(urlutil.URL.TYSX_LOGIN)

        pass
    def tearDown(self):
        # 关闭浏览器
        self.brower.CloseChrom()
        pass






    # 用户名为空，密码为空
   # def test_phonenum_em_pw_em(self):





    #     u"""手机号为空,密码为空,应该提示--手机号：不能为空"""
    #     self.brower.FindId("uname").clear()
    #     self.brower.FindId("upwd").clear()
    #     self.brower.FindClass("login-btn").click()
    #     time.sleep(3)
    #
    #     self.assertEqual(self.brower.FindClass("lm-logintips-box").text, u"手机号：不能为空")


        # # 清除手机号
        # self.phonenum.clear()
        # # 清除密码
        # self.password.clear()
        # # 点击登录按钮
        # self.login.click()
        # # 智能休眠
        # self.driver.implicitly_wait(5)
        # # 查找显示出来的控件 提示框
        # # 查找提示框的控件（用来断言）
        # self.msg_error=self.driver.find_element_by_class_name("lm-logintips-box")
        # # 获取内容
        # self.text=self.msg_error.text
        # # 使用断言来判断是不是需要的内容
        # self.assertEqual(self.text,u"手机号：不能为空")

        # pass
        # 手机号不为空但手机号输入不正确，密码为空
    # def test_phoen_fail_pwd_em(self):
    #         u"""手机号不为空但输入不正确,密码为空,应该提示--手机号：请输入正确手机号"""
    #         self.brower.FindId("uname").send_keys("15111")
    #         self.brower.FindId("upwd").clear()
    #         self.brower.FindId("uname").click()
    #
    #
    #         self.text1=self.brower.FindClass("lm-logintips-box").text
    #         self.assertEqual(self.text1, u"手机号：请输入正确手机号")
    #         time.sleep(2)
    #         self.brower.FindClass("login-btn").click()
    #         time.sleep(2)
    #         self.text2 = self.brower.FindClass("lm-logintips-box").text
    #         self.assertEqual(self.text2, u"密码：不能为空")

            # # 输入手机号
            # self.phonenum.send_keys("15111")
            # # 清除密码
            # self.password.clear()
            #
            # # 点击输入框
            # self.phonenum.click()
            # # 查找提示框的控件
            # self.msg_error1 = self.driver.find_element_by_class_name("lm-logintips-box")
            # # 获取内容
            # self.text1 = self.msg_error1.text
            # # 使用断言来判断是不是需要的内容
            # self.assertEqual(self.text1, u"手机号：请输入正确手机号")
            # # 进行智能休眠
            # self.driver.implicitly_wait(5)
            #
            # # 点击登录按钮
            # self.login.click()
            # # 进行智能休眠
            # self.driver.implicitly_wait(5)
            #
            # # 查找提示框的控件
            # self.msg_error=self.driver.find_element_by_class_name("lm-logintips-box")
            # # 获取内容
            # self.text=self.msg_error.text
            # # 使用断言来判断是不是需要的内容
            # self.assertEqual(self.text,u"密码：不能为空")
            # pass


    # # 手机号输入正确，密码为空
    # def test_phone_right_pw_em(self):
    #      u"""手机号不为空，输入正确,密码为空,应该提示--密码：不能为空"""
    #      self.brower.FindId("uname").send_keys("15111111111")
    #      self.brower.FindId("upwd").clear()
    #      self.brower.FindClass("login-btn").click()
    #      time.sleep(2)
    #      self.text=self.brower.FindClass("lm-logintips-box").text
    #      self.assertEqual(self.text,u"密码：不能为空")





    #     # 输入手机号
    #     self.phonenum.send_keys("15111111111")
    #     # 清除密码
    #     self.password.clear()
    #     # 点击登录
    #     self.login.click()
    #
    #     # 进行智能休眠
    #     self.driver.implicitly_wait(5)
    #
    #     # 查找提示框的控件
    #     self.msg_error = self.driver.find_element_by_class_name("lm-logintips-box")
    #     # 获取内容
    #     self.text = self.msg_error.text
    #     # 使用断言来判断是不是需要的内容
    #     self.assertEqual(self.text, u"密码：不能为空")
    #
    # 手机号输入正确，密码输入不正确
    # def test_phone_right_pw_fail(self):
    #       u"""手机号输入正确,密码输入长度<6,应该提示--密码：长度6-20位(数字/字母/下划线)"""
    #       self.brower.FindId("uname").send_keys("15111111111")
    #       self.brower.FindId("upwd").send_keys(123)
    #       self.brower.FindClass("login-btn").click()
    #       time.sleep(2)
    #       self.text = self.brower.FindClass("lm-logintips-box").text
    #       self.assertEqual(self.text, u"密码：长度6-20位(数字/字母/下划线)")






    #      # 输入手机号
    #      self.phonenum.send_keys("15111111111")
    #      # 输入密码
    #      self.password.send_keys("1234")
    #      # 点击登录
    #      self.login.click()
    #      # 智能休眠
    #      self.driver.implicitly_wait(5)
    #      # 查找提示框的控件
    #      self.msg_error=self.driver.find_element_by_class_name("lm-logintips-box")
    #      # 获取内容
    #      self.text=self.msg_error.text
    #      # 使用断言来判断是不是需要的内容
    #      self.assertEqual(self.text,u"密码：长度6-20位(数字/字母/下划线)")
    #
    #      pass
    # # 手机号输入正确，密码输入不正确
    # def test_phone_right_pw_fail(self):
    #
    #   u"""手机号输入正确,密码输入长度>=6且不正确,应该提示--登录失败，密码错误"""
    #   self.brower.FindId("uname").send_keys("15111111111")
    #   self.brower.FindId("upwd").send_keys(1234567)
    #   self.brower.FindClass("login-btn").click()
    #   time.sleep(2)
    #   self.text = self.brower.FindClass("lm-logintips-box").text
    #   self.assertEqual(self.text, u"登录失败，密码错误")

















    #  # 输入手机号
    #  self.phonenum.send_keys("15111111111")
    #  # 输入密码
    #  self.password.send_keys("123456")
    #  # 点击登录
    #  self.login.click()
    #  # 智能休眠
    #  self.driver.implicitly_wait(5)
    #
    #  # 查找提示框的控件
    #  self.msg_error=self.driver.find_element_by_class_name("lm-logintips-box")
    #  # 获取内容
    #  self.text=self.msg_error.text
    #  # 使用断言判断是不是需要的内容
    #  self.assertEqual(self.text,u"登录失败，密码错误")
    #
    # pass
    #
     # 手机号输入正确，密码输入正确
    def test_phone_right_pw_right(self):
         u"""手机号输入正确,密码输入正确,跳转首页"""
         self.brower.FindId("uname").send_keys("15111111111")
         self.brower.FindId("upwd").send_keys(111111)
         self.brower.FindClass("login-btn").click()
         time.sleep(2)

         self.assertEqual(self.brower.driver.title, u"个人中心")

















    #
    #     # 输入手机号
    #     self.phonenum.send_keys("15111111111")
    #     # 输入密码
    #     self.password.send_keys("111111")
    #     # 点击登录
    #     self.login.click()
    #     # 智能休眠
    #     time.sleep(5)
    #
    #     # 使用断言判断是不是需要的内容
    #     self.assertEqual(self.driver.title,u"个人中心")
    #
    #     pass
