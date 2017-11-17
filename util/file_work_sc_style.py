# -*- coding:utf-8 -*-
import time
# 上传图片方法
def Sc_Picture(self):
    # 点击上传图片按钮
    self.brower.FindId("wd_radio_zdfs-sctp").click()
    # 输入试题数量
    self.brower.FindClasses("J_zyxx_stsl")[0].send_keys("1")
    time.sleep(3)
    # 输入总分（小数）
    self.brower.FindClasses("J_zyxx_zf")[0].send_keys(".")
    time.sleep(3)
    self.assertEqual(self.brower.FindId("zftips").text, u"请录入整数（1-150）")
    time.sleep(3)
    # 输入总分（>150）
    self.brower.FindClasses("J_zyxx_zf")[0].send_keys("200")
    time.sleep(3)
    self.assertEqual(self.brower.FindId("zftips").text, u"请录入整数（1-150）")
    time.sleep(3)
    # 输入总分（<=150 且 >=1）
    self.brower.FindClasses("J_zyxx_zf")[0].send_keys("10")
    time.sleep(3)

# 上传答案方法
def Sc_Result(self):
    # 点击上传答案按钮
    self.brower.FindId("wd_radio_zdfs-srda").click()
    time.sleep(3)
    # 点击输入试题数量 输入为小于1
    self.brower.FindClasses("J_srda_stsl")[0].send_keys("0")
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("stsltipsForSrda").text, u"请录入整数（1-99）")
    time.sleep(3)
    # 输入试题数量 大于99
    self.brower.FindClasses("J_srda_stsl")[0].send_keys("100")
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("stsltipsForSrda").text, u"请录入整数（1-99）")
    # 输入试题数量大于1并且小于99
    self.brower.FindClasses("J_srda_stsl")[0].send_keys("2")
    time.sleep(3)
    # 输入试题的正确答案
    self.brower.FindClasses("J_srda_zqda")[0].click()
    time.sleep(3)
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[2]/td[2]").click()
    time.sleep(3)

    self.brower.FindClasses("J_srda_zqda")[1].click()
    time.sleep(3)
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(3)
    # 输入分值
    self.brower.FindClasses("J_srda_xztFz")[0].send_keys("10")



