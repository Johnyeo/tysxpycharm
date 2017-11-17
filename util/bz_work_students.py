# -*- coding:utf-8 -*-
import  time
def bz_work_Students(self):
    # 布置作业
    # 切换到按学生
    self.brower.FindLink_text("按学生").click()
    time.sleep(3)
    # 设置作业提交截止时间
    self.brower.FindId("J_zyjzsj").click()
    time.sleep(3)
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_17").click()
    time.sleep(3)
    # 点击全选框  进行全选
    self.brower.FindXpath("//*[@id='wd_checkBox_248439809012535302_3000008250']").click()
    time.sleep(3)
    # 点击确认 布置作业成功
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(5)
    # 断言 是否跳转成功
    self.assertEqual(self.brower.driver.title, u"作业管理")

