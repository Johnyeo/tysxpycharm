# -*- coding:utf-8 -*-
import  time
# 共享作业
from util import share_work,cancle_share_work

def NewsWokd(self):
    # 点击待批作业按钮 在没有待批作业的情况下
    self.brower.FindClasses("J_btn_dp")[2].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"无待批作业！")
    time.sleep(3)
    # 点击关闭
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(3)
    # 修改作业提交截止时间
    self.brower.FindClasses("J_btn_jzsj")[0].click()
    time.sleep(3)
    # 点击下拉框
    self.brower.FindClasses("J_date_zyjzsj")[0].click()
    time.sleep(3)
    # 点击清空
    self.brower.FindXpath("//*[@id='dateLayer']/div/div[3]/button[3]").click()
    # 再次点击下拉框
    self.brower.FindClasses("J_date_zyjzsj")[0].click()
    time.sleep(3)
    # 选择截止时间  选择时间少于当前时间
    self.brower.FindId("_0_1").click()
    self.brower.FindClass("wd-prompt-body").click()
    time.sleep(3)
    # 修改完成后 点击确定
    self.brower.FindClass("J_btn_confirm_zyjzsj").click()
    time.sleep(3)
    # 弹框提示
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"作业提交截止时间不能小于当前时间！")
    time.sleep(3)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(3)
    # 再次点击下拉框选择截止时间
    self.brower.FindClasses("J_date_zyjzsj")[0].click()
    time.sleep(3)
    # 点击清空
    self.brower.FindXpath("//*[@id='dateLayer']/div/div[3]/button[3]").click()
    # 再次点击下拉框
    self.brower.FindClasses("J_date_zyjzsj")[0].click()
    time.sleep(3)
    # 选择截止时间  选择时间少于当前时间
    self.brower.FindId("_30").click()
    self.brower.FindClass("wd-prompt-body").click()
    time.sleep(3)
    # 修改完成后 点击确定
    self.brower.FindClass("J_btn_confirm_zyjzsj").click()
    time.sleep(3)
    # 共享作业 没有学校的老师
    #share_work.NewWork_ShreWorkNoS(self)
    # 共享作业 有学校的老师
    share_work.NewWork_ShareWorkS(self)
    # 取消共享
    cancle_share_work.CancleShareWork(self)


