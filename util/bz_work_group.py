# -*- coding:utf-8 -*-
import  time
def bz_work_Group(self):
    # 布置作业
    # 切换按小组布置作业
    self.brower.FindLink_text("按小组").click()
    time.sleep(3)
    # 设置作业提交截止时间
    self.brower.FindId("J_zyjzsj").click()
    time.sleep(3)
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_17").click()
    time.sleep(3)
    # 选择某个班级--班级内无小组
    self.brower.FindClasses("load")[0].click()
    time.sleep(2)
    # 点击确认按钮
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(3)
    # 弹框提示
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"您还没有选择小组！")
    time.sleep(3)
    # 点击关闭弹框
    self.brower.FindNmae("wd_dialog_alert").click()
    time.sleep(3)
    # 点击全选框  进行全选
    # qbxz = self.brower.FindClass("qbxz")
    # checkboxes = qbxz.find_elements_by_class_name("wd-checkbox-check")
    # checkboxes[0].click()
    self.brower.FindXpath("//*[@id='wd_checkBox_248440005519872006']").click()
    time.sleep(3)

    # 点击确认 布置作业成功
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(3)
    # 断言 是否跳转成功
    self.assertEqual(self.brower.driver.title, u"作业管理")
