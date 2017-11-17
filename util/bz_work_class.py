# -*- coding:utf-8 -*-
import  time
def bz_work_Class(self):
    # 布置作业
    # 按班级布置作业
    # 设置作业提交截止时间
    self.brower.FindClass("Wdate").click()
    time.sleep(3)
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_0_2").click()
    time.sleep(3)
    # 点击确定按钮
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(3)
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"作业提交截止时间不能小于当前时间！")
    time.sleep(3)
    # 关闭弹框
    self.brower.FindNmae("wd_dialog_alert").click()
    time.sleep(3)

    # 再次设置作业提交截止时间
    self.brower.FindClass("Wdate").click()
    time.sleep(3)
    # 清空时间
    self.brower.FindXpath("//*[@id='dateLayer']/div/div[3]/button[3]").click()
    time.sleep(3)
    # 再点击设置时间的下拉框
    self.brower.FindClass("Wdate").click()
    time.sleep(3)
    # 选择作业提交的截止时间/
    self.brower.FindId("J_zyjzsj_17").click()
    time.sleep(3)
    # 反选
    self.brower.FindId("wd_checkBox_wdcheckall-bzzybox").click()
    time.sleep(3)
    # # 勾选某一个班级--班级人数为空    所选班级内无学生，请确认！
    # self.brower.FindXpath("//*[@id='wd_checkBox_239771277055889415']").click()
    # time.sleep(3)
    # # 点击确定按钮
    # self.brower.FindClass("J_btn_confirm").click()
    # time.sleep(3)
    # # 弹框提示--班内没有学生
    # self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"所选班级内无学生，请确认！")
    # time.sleep(3)
    # # 点击关闭按钮
    # self.brower.FindId("prompt-wd_prompt_close-alert").click()
    # time.sleep(3)
    # # 反选
    # self.brower.FindXpath("//*[@id='wd_checkBox_239771277055889415']").click()
    # time.sleep(3)
    # 勾选某一个班级--班级人数不为空
    self.brower.FindXpath("//*[@id='wd_checkBox_247735889676079104']").click()
    time.sleep(3)
    # 点击确定按钮 布置成功跳转
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(5)
    # 断言
    self.assertEqual(self.brower.driver.title, u"作业管理")
    time.sleep(5)
