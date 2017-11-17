# -*- coding:utf-8 -*-
import time
# 保存 修改文件作业 上传方式
from util import file_work_sc_style
def UpdateFileWork(self):
    # 修改保存作业--文件作业
    # 点击修改按钮
    self.brower.FindLink_text("修改").click()
    # 跳转到发布文件作业页面
    time.sleep(3)
    self.assertEqual(self.brower.driver.title, u"发作业-文件作业")
    time.sleep(3)
    # 修改文件作业上传方式为---输入答案
    file_work_sc_style.Sc_Result(self)
    # 修改完成后点击保存 或布置作业
    # 点击保存
    # 点击保存
    self.brower.FindId("J_btn_bc").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.driver.title, u"作业管理")

def UpdateStWork(self):
    # 修改保存作业--试题作业
    # 点击修改按钮
    self.brower.FindLink_text("修改").click()
    # 跳转到发布试题作业页面
    time.sleep(3)
    self.assertEqual(self.brower.driver.title, u"发作业-试题作业")
    # 修改第一大题选择题的分数
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[1]/div[1]/p/input").clear()
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[1]/div[1]/p/input").send_keys("5")
    # 点击保存试题
    self.brower.FindClasses("bg-default")[0].click()
    time.sleep(3)
    # 点击确定按钮 跳转到作业管理首页
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    self.assertEqual(self.brower.driver.title, u"作业管理")