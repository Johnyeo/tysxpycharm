# -*- coding:utf-8 -*-
import time
from util import urlutil
def LookFileWork(self):
    # 点击查看文件作业名称
    self.brower.FindXpath("//*[@id='zylbcontent']/div[1]/dl[2]/dt/h4/a").click()
    time.sleep(3)
    urlutil.switch_window_to(self.brower.driver, u"查看文件作业")
    # 断言
    self.assertEqual(self.brower.driver.title,u"查看文件作业")
    time.sleep(3)
    # 点击作业管理回到上一页面
    self.brower.FindXpath("//*[@id='ckwjzy']/div/ul/li[2]/a").click()
    # 断言
    self.assertEqual(self.brower.driver.title,u"作业管理")
    time.sleep(5)
