# -*- coding:utf-8 -*-
import time
import st_work
def bzWork(self):
    st_work.stWork(self)
    # 点击布置作业
    self.brower.FindClasses("J_btn_bz")[0].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"本作业的总分为80.0分!")
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)

    # 按班级布置作业
    # 设置作业提交截止时间
    self.brower.FindClass("Wdate").click()
    time.sleep(3)
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_21").click()
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
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_32").click()
    time.sleep(3)
    # 勾选全选按钮
    self.brower.FindId("wd_checkBox_wdcheckall-bzzybox").click()
    time.sleep(2)
    # 反选
    self.brower.FindId("wd_checkBox_wdcheckall-bzzybox").click()
    time.sleep(3)
    # 勾选某一个班级--班级人数为空    所选班级内无学生，请确认！
    self.brower.FindClasses("wd-checkbox-lable")[1].click()
    time.sleep(3)
    # 点击确定按钮
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(3)
    # 弹框提示--班内没有学生
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"所选班级内无学生，请确认！")
    time.sleep(3)
    # 点击关闭按钮
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(3)
    # 反选
    self.brower.FindClasses("wd-checkbox-lable")[1].click()
    time.sleep(3)
    # 勾选某一个班级--班级人数不为空
    self.brower.FindClasses("wd-checkbox-lable")[3].click()
    time.sleep(3)
    # 点击确定按钮 布置成功跳转
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(5)
    # 断言
    self.assertEqual(self.brower.driver.title, u"作业管理")
    time.sleep(5)

    # 按小组布置作业
    st_work.stWork(self)
    # 点击布置作业
    self.brower.FindClasses("J_btn_bz")[0].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"本作业的总分为80.0分!")
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(5)
    # 切换按小组布置作业
    self.brower.FindLink_text("按小组").click()
    time.sleep(3)
    # 设置作业提交截止时间
    self.brower.FindClass("Wdate").click()
    time.sleep(3)
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_32").click()
    time.sleep(3)
    # 选择某个班级--班级内无小组
    self.brower.FindClasses("load")[0].click()
    time.sleep(3)
    # 点击确认按钮
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(3)
    # 弹框提示
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"您还没有选择小组！")
    time.sleep(3)
    # 点击关闭弹框
    self.brower.FindNmae("wd_dialog_alert").click()
    time.sleep(3)
    # 选择另外某个班级
    self.brower.FindXpath("//*[@id='wd-prompt-textarea']/div/div[2]/div[3]/div/div[1]/ul/li[3]").click()
    time.sleep(5)
    # 点击全选框  进行全选
    qbxz = self.brower.FindClass("qbxz")
    checkboxes = qbxz.find_elements_by_class_name("wd-checkbox-check")
    checkboxes[0].click()
    time.sleep(3)
    # 点击确认 布置作业成功
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(5)
    # 断言 是否跳转成功
    self.assertEqual(self.brower.driver.title, u"作业管理")
    time.sleep(5)
    # 按学生布置作业
    st_work.stWork(self)
    # 点击布置作业
    self.brower.FindClasses("J_btn_bz")[1].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"本作业的总分为80.0分!")
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(5)

    # 按学生布置
    st_work.stWork(self)
    # 点击布置作业
    self.brower.FindClasses("J_btn_bz")[0].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"本作业的总分为80.0分!")
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(5)
    # 切换到按学生
    self.brower.FindLink_text("按学生").click()
    time.sleep(3)
    # 设置作业提交截止时间
    self.brower.FindClass("Wdate").click()
    time.sleep(3)
    # 选择作业提交的截止时间
    self.brower.FindId("J_zyjzsj_32").click()
    time.sleep(3)
    # 选择某一个班级
    self.brower.FindXpath("//*[@id='wd-prompt-textarea']/div/div[2]/div[4]/div/div[1]/ul/li[3]").click()
    time.sleep(3)
    # 点击全选框  进行全选
    qbxz = self.brower.FindClass("qbxz")
    checkboxes = qbxz.find_elements_by_class_name("wd-checkbox-check")
    checkboxes[0].click()
    time.sleep(3)
    # 点击确认 布置作业成功
    self.brower.FindClass("J_btn_confirm").click()
    time.sleep(5)
    # 断言 是否跳转成功
    self.assertEqual(self.brower.driver.title, u"作业管理")
    time.sleep(5)



