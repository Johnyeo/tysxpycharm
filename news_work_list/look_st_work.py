# -*- coding:utf-8 -*-
from util import urlutil
import time
def LookStWork(self):
    # 点击查看试题
    self.brower.FindLink_text("查看").click()
    time.sleep(3)
    urlutil.switch_window_to(self.brower.driver,u"查看试题作业结果")
    # 断言
    self.assertEqual(self.brower.driver.title, u"查看试题作业结果")
    # 通过导航选择查看的试题
    # 点击选择题
    self.brower.FindLink_text("一、选择题").click()
    time.sleep(3)
    # 查看答案解析
    self.brower.FindLink_text("查看答案解析").click()
    time.sleep(3)
    # 隐藏答案解析
    self.brower.FindLink_text("隐藏答案解析").click()
    time.sleep(3)
    urlutil.switch_window_to(self.brower.driver, u"作业管理")
    time.sleep(3)






