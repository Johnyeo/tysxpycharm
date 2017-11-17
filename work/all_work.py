# -*- coding:utf-8 -*-
import time
# 布置作业
from util import bz_work_students
# 修改作业
from util import update_work
# 共享作业
from util import share_work
# 返回原来页面
from util import urlutil
# 查看试题作业详情
from news_work_list import look_st_work
def AllWork(self):
    # 点击切换到全部作业页面
    self.brower.FindId("J_tab_qbzy").click()
    time.sleep(3)
    # 通过输入作业名称模糊查询
    self.brower.FindId("J_query_zymc").send_keys(u"自动化试题作业")
    time.sleep(3)

    # 通过年级查询
    # 点击年级下拉框
    self.brower.FindId("code_NJ").click()
    # 选择七年级进行查询
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(3)
    # 选择册别
    # 点击册别下拉框
    self.brower.FindId("code_CB").click()
    # 选择上册进行查询
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(3)
    # 点击查询
    self.brower.FindId("searchBtn").click()
    time.sleep(3)

    # 点击查看
    # 查看试题作业
    self.brower.FindLink_text("查看").click()
    time.sleep(3)
    urlutil.switch_window_to(self.brower.driver, u"作业动态")
    # 断言
    self.assertEqual(self.brower.driver.title,u"作业动态")
    time.sleep(3)
    # 查看试题作业
    look_st_work.LookStWork(self)
    # 点击切换到全部作业页面
    self.brower.FindId("J_tab_qbzy").click()
    time.sleep(3)

    # 点击修改按钮 修改试题作业 进入到发布作业页面
    update_work.UpdateStWork(self)
    # 点击删除按钮 (提交人数为0事可以删除)
    self.brower.FindLink_text("删除").click()
    time.sleep(3)
    # 弹框提示--是否确定删除作业
    # 断言验证
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"确定删除作业？")
    time.sleep(3)
    # 点击确定按钮  删除成功
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    # 共享作业
    share_work.AllWork_ShreWorkS(self)
    time.sleep(3)
    # 点击切换到全部作业页面
    self.brower.FindId("J_tab_qbzy").click()
    time.sleep(3)
    # # 点击查看-文件作业 （提交人数大于0时） 跳转到作业动态页面
    # # 通过输入作业名称模糊查询
    # self.brower.FindId("J_query_zymc").send_keys(u"自动化文件作业")
    # time.sleep(3)
    # # 点击查询
    # self.brower.FindId("searchBtn").click()
    # time.sleep(3)
    # self.brower.FindLink_text("查看").click()
    # time.sleep(3)
    # urlutil.switch_window_to(self.brower.driver, u"作业动态")
    # time.sleep(3)
    # # 断言
    # self.assertEqual(self.brower.driver.title, u"作业动态")
    # time.sleep(3)
    # # 点击查看跳转到查看文件作业结果
    # self.brower.FindLink_text("查看").click()
    # urlutil.switch_window_to(self.brower.driver, u"查看文件作业结果")
    # time.sleep(3)
    # # 断言
    # self.assertEqual(self.brower.driver.title, u"查看文件作业结果")
    # time.sleep(3)
    # # 查看文件作业结果
    # # 点击图片 可以对图片进行放大 拖动
    # self.brower.FindClass("viewer-toggle").click()
    # time.sleep(3)
    # # 点击关闭
    # self.brower.FindClasses("viewer-close")[0].click()
    # time.sleep(3)
    # # 在很多张图片的情况下 可以点击向左 向右展示
    # # 向右点击
    # self.brower.FindClasses("fr")[0].click()
    # time.sleep(3)
    # # 点击作业管理 返回原页面
    # self.brower.FindXpath("//*[@id='zyjg-wj']/div/ul/li[2]/a").click()
    # time.sleep(3)
    # self.assertEqual(self.brower.driver.title, u"作业管理")
    # # 点击切换到全部作业页面
    # self.brower.FindId("J_tab_qbzy").click()
    # time.sleep(3)
    # # 点击加精作业图标
    # self.brower.FindXpath("//*[@id='table_qbzylb']/tbody/tr[2]/td[1]/span/em[1]").click()
    # time.sleep(3)
    # self.brower.FindXpath("//*[@id='table_qbzylb']/tbody/tr[3]/td[1]/span/em[1]").click()
    # time.sleep(3)
    # # 点击隐藏作业图标
    # self.brower.FindXpath("//*[@id='table_qbzylb']/tbody/tr[6]/td[1]/span/em[2]").click()
    # time.sleep(3)
    # self.brower.FindXpath("//*[@id='table_qbzylb']/tbody/tr[7]/td[1]/span/em[2]").click()
    # time.sleep(3)
    # 点击勾选 只显示加精作业
    self.brower.FindId("wd_checkBox_J_qbzy_jj").click()
    time.sleep(3)
    # 反选
    self.brower.FindId("wd_checkBox_J_qbzy_jj").click()
    time.sleep(3)
    # 点击勾选 不显示隐藏作业
    self.brower.FindId("wd_checkBox_J_qbzy_yc").click()
    time.sleep(3)