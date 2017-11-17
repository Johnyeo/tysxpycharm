# -*- coding:utf-8 -*-
import time
import news_file_work
def CancleFileWork(self):
    news_file_work.NewsWork(self)
    # 点击取消
    self.brower.FindId("J_btn_qx").click()
    time.sleep(3)
    self.assertEqual(self.brower.driver.title, u"作业管理")