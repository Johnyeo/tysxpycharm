# -*- coding:utf-8 -*-
import time
import st_work
import news_file_work
def save_st_Work(self):
    st_work.stWork(self)
    # 点击保存试题
    self.brower.FindClasses("bg-default")[0].click()
    time.sleep(3)
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text,u"本作业的总分为50.0分!")
    time.sleep(3)
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    self.assertEqual(self.brower.driver.title,u"作业管理")

def SaveFileWork(self):
    news_file_work.NewsWork(self)
    # 点击保存
    self.brower.FindId("J_btn_bc").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.driver.title, u"作业管理")