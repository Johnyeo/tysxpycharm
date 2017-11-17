# -*- coding:utf-8 -*-
import time
import win32api
import file_work_sc_style
import shangc_file_style_work

a = 1
b = 2

def NewsWork(self):
    u"""发布文件作业"""
    # 点击发作业按钮
    time.sleep(a)
    self.brower.FindXpath("/html/body/div[2]/div[1]/div/div/input").click()
    time.sleep(a)
    # 点击文件作业
    self.brower.FindClasses("btn-nbi")[1].click()
    time.sleep(a)
    self.assertEqual(self.brower.driver.title, u"发作业-文件作业")
    # 休眠
    time.sleep(a)
    time.sleep(a)
    # 作业标题为空
    self.brower.FindClasses("J_zyxx_zybt")[0].clear()
    self.brower.FindClasses("J_zyxx_zybt")[0].click()
    time.sleep(a)
    self.assertEqual(self.brower.FindId("zybttips").text, u"作业标题：不能为空")
    # 作业标题不为空
    time.sleep(a)
    self.brower.FindClasses("J_zyxx_zybt")[0].send_keys(u"自动化文件作业")
    time.sleep(a)
    # 选择年级
    # 定位到下拉框
    self.brower.FindId("code_nj").click()
    # 再点击下拉框的选项
    self.brower.FindClass("DMRB2").click()
    time.sleep(a)
    # 选择册别
    # 定位到下拉框
    self.brower.FindId("code_cb").click()
    # 再点击下拉框的选项
    self.brower.FindClass("DMRB2").click()
    # 休眠
    time.sleep(a)
    # 选择章节目录
    # 定位到下拉框
    self.brower.FindId("mulu").click()
    # 再点击下拉框的选项
    self.brower.FindClass("inactive").click()
    # 休眠
    time.sleep(a)
    win32api.keybd_event(34, 0, 0, 0)

    time.sleep(a)
    # 选择作答方式
    # 上传图片
    file_work_sc_style.Sc_Picture(self)
    # # 上传答案
    # file_work_sc_style.Sc_Result(self)
    # time.sleep(a)
    # 输入作业内容
    self.brower.FindClasses("J_zyxx_zynr")[0].send_keys(u"输入作业内容")
    # 休眠
    time.sleep(a)

    #上传本地文件
    shangc_file_style_work.BendFileWork(self)



