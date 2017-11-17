# -*- coding:utf-8 -*-
import time
from util import bz_work_students
def ShareWork(self):
    # 点击切换到本校共享作业页面
    self.brower.FindId("J_tab_bxgxzy").click()
    time.sleep(3)
    # 通过作业名称进行模糊查询
    self.brower.FindId("J_query_zymc").send_keys(u"自动化试题")
    time.sleep(3)
    # 点击查询 查询结果展示页面
    self.brower.FindId("searchBtn").click()
    time.sleep(3)
    # 通过作业类型
    self.brower.FindId("code_ZYLX").click()
    time.sleep(3)
    # 选择试题作业类型
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(3)
    # 点击查询 查询结果展示页面
    self.brower.FindId("searchBtn").click()
    time.sleep(3)
    # 可以将老师分享的作业 再进项布置
    # 点击布置按钮--试题作业
    self.brower.FindClass("pink").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.driver.title, u"发作业-试题作业")
    time.sleep(3)
    # 点击布置按钮 按学生布置作业
    self.brower.FindClasses("J_btn_bz")[0].click()
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    bz_work_students. bz_work_Students(self)