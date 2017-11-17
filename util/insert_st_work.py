# -*- coding:utf-8 -*-
import time
import st_work
def Insert_st_Work(self):
    st_work.stWork(self)
    # 点击添加试题
    self.brower.FindClasses("J_btn_jt")[0].click()
    time.sleep(3)
    # 点击选择题类型
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[1]/div/span[1]").click()
    time.sleep(3)
    # 选择试题
    self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[2]/td/div/div[1]/div[2]/input").click()
    time.sleep(3)
    # 点击确定
    self.brower.FindClasses("xzlxt-qd-btn")[0].click()
    time.sleep(3)
    self.assertEqual(self.brower.driver.title, u"发作业-试题作业")

