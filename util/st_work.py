# -*- coding:utf-8 -*-
import time

import win32api

from selenium.common.exceptions import ElementNotVisibleException
from win32con import MOUSEEVENTF_LEFTDOWN

a = 2
b = 4

def scrollDown(holdsec):
    win32api.keybd_event(0x22, 0, 0, 0)
    time.sleep(holdsec)

def scrolltToEnd(holdsec):
    win32api.keybd_event(0x23, 0, 0, 0)
    time.sleep(holdsec)

def scrollToHome(holdsec):
    win32api.keybd_event(0x24, 0, 0, 0)
    time.sleep(holdsec)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(2,x,y,0,0)
    win32api.mouse_event(4,x,y,0,0)


def stWork(self):
    # 发布试题作业
    # 点击发布作业
    self.brower.FindClasses("btn-fbzy")[0].click()
    time.sleep(a)
    # 点击发试题作业
    self.brower.FindClasses("btn-nbi")[0].click()
    time.sleep(b)
    # 点击确定
    self.brower.FindClasses("xzlxt-qd-btn")[0].click()
    time.sleep(a)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"请先选择试题")
    time.sleep(a)
    # 点击关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(b)

    # 知识点
    # 选择年级
    self.brower.FindId("codeXzlxt_NJLXT").click()
    time.sleep(a)
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(a)
    # 选择册别
    self.brower.FindId("codeXzlxt_CBLXT").click()
    time.sleep(a)
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(a)
    # 选择章节目录
    self.brower.FindXpath("//*[@id='xzlxt-ml-menu']/div/ul/li[1]/a").click()
    time.sleep(a)
    self.brower.FindXpath("//*[@id='xzlxt-ml-menu']/div/ul/li[1]/ul/li[1]/a").click()
    time.sleep(a)
    self.brower.FindXpath("//*[@id='xzlxt-ml-menu']/div/ul/li[1]/ul/li[1]/ul/li[1]/a").click()
    time.sleep(b)

    # 选择试题的题型
    # 点击选择题
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[1]/div/span[1]").click()
    time.sleep(a)
    # 选择填空题
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[1]/div/span[2]").click()
    time.sleep(a)
    # 选择解答题
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[1]/div/span[3]").click()
    time.sleep(a)
    # 选择题型难度
    # 点击中等
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[2]/div/span[2]").click()
    time.sleep(a)
    # 反选中等
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[2]/div/span[2]").click()
    time.sleep(a)
    # 选择试题类别
    # 全国试题
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[3]/div/span[1]").click()
    time.sleep(a)
    # 导入标题 查询标题 --支持模糊查询
    self.brower.FindXpath("//*[@id='drbtVal']").send_keys("yy")
    # 点击查询
    self.brower.FindClass("daorusousuoval").click()
    time.sleep(a)
    # 清空输入框内容
    self.brower.FindXpath("//*[@id='drbtVal']").clear()
    # 点击查询
    self.brower.FindClass("daorusousuoval").click()
    time.sleep(a)
    # 创建人查询--支持模糊查询
    self.brower.FindXpath("//*[@id='drrVal']").send_keys(u"小梁")
    # 点击查询
    self.brower.FindClass("daorusousuoval").click()
    time.sleep(a)
    # 清空输入框内容
    self.brower.FindXpath("//*[@id='drrVal']").clear()
    # 点击查询
    self.brower.FindClass("daorusousuoval").click()
    time.sleep(a)
    # 选择试题类别
    # 全国试题
    self.brower.FindXpath("//*[@id='xzlxt-main-list']/div[2]/ul/li[3]/div/span[1]").click()
    time.sleep(a)
    # 选择试题
    self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[2]/td/div/div[1]/div[2]/input").click()
    time.sleep(a)
    # 尝试点击，如果抛出找不到元素的异常，就激发“Pagedown"按键，再点击。
    try:
        self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[3]/td/div/div[1]/div[2]/input").click()
    except ElementNotVisibleException as e:
        print('element not visiable, auto click pagedown')
        click(500, 500)
        scrollDown(b)
        self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[3]/td/div/div[1]/div[2]/input").click()
    time.sleep(a)

    try:
        self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[4]/td/div/div[1]/div[2]/input").click()
    except ElementNotVisibleException as e:
        print('element not visiable, auto click pagedown')
        scrollDown(b)
        self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[4]/td/div/div[1]/div[2]/input").click()
    time.sleep(a)

    try:
        self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[5]/td/div/div[1]/div[2]/input").click()
    except ElementNotVisibleException as e:
        print('element not visiable, auto click pagedown')
        scrollDown(b)
        self.brower.FindXpath("//*[@id='table_xzlxt']/tbody/tr[5]/td/div/div[1]/div[2]/input").click()
    time.sleep(a)

    # 点击确定
    self.brower.FindClasses("xzlxt-qd-btn")[0].click()
    time.sleep(a)
    self.assertEqual(self.brower.driver.title, u"发作业-试题作业")
    time.sleep(a)

    # 跳转到发作业界面
    # 作业标题为空
    self.brower.FindClasses("input-style-search")[0].clear()
    time.sleep(a)
    self.brower.FindClasses("input-style-search")[0].click()
    time.sleep(a)
    self.assertEqual(self.brower.FindClass("messagetips").text, u"作业标题：不能为空")
    time.sleep(a)
    # 作业标题不为空
    self.brower.FindClasses("input-style-search")[0].send_keys(u"自动化试题作业")
    time.sleep(a)
    # 选择年级 点击下拉菜单
    self.brower.FindId("code_nj").click()
    #  选中年级
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(a)
    # 选择册别 点击下拉框
    self.brower.FindId("code_cb").click()
    # 选中册别
    self.brower.FindXpath("//*[@id='dmBody']/tbody/tr[1]/td[2]").click()
    time.sleep(a)
    # # 选择章节目录 点击下拉框
    self.brower.FindId("mulu").click()
    self.brower.FindClass("rem").click()
    self.brower.FindXpath("//*[@id='zjml_content']/div/div/ul/li[1]/ul/li[1]/a/p").click()
    time.sleep(b)
    time.sleep(b)
    # 未填写分值 点击保存
    self.brower.FindClasses("bg-default")[0].click()
    time.sleep(a)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"选择题第1题的分数需要输入，请输入大于0且不大于100的分值！")
    time.sleep(a)
    # 点击关闭
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(a)
    # 清空分值
    self.brower.FindClasses("J_input_fz")[0].clear()
    time.sleep(a)
    # 填写分值  选择题
    self.brower.FindClasses("J_input_fz")[0].send_keys(".")
    self.brower.FindClasses("J_input_fz")[0].send_keys("150")
    self.brower.FindClasses("J_input_fz")[0].send_keys("10")
    time.sleep(a)
    # 填写分值 填空题
    try:
        self.brower.FindClasses("J_input_fz")[1].send_keys(".")
        self.brower.FindClasses("J_input_fz")[1].send_keys("150")
        self.brower.FindClasses("J_input_fz")[1].send_keys("10")
        time.sleep(a)

    except ElementNotVisibleException as e:
        win32api.keybd_event(34, 0, 0, 0)
        time.sleep(b)
        self.brower.FindClasses("J_input_fz")[1].send_keys(".")
        self.brower.FindClasses("J_input_fz")[1].send_keys("150")
        self.brower.FindClasses("J_input_fz")[1].send_keys("10")
        time.sleep(a)

    try:
        self.brower.FindClasses("J_input_fz")[2].send_keys(".")
        self.brower.FindClasses("J_input_fz")[2].send_keys("150")
        self.brower.FindClasses("J_input_fz")[2].send_keys("10")
        time.sleep(a)

    except ElementNotVisibleException as e:
        win32api.keybd_event(34, 0, 0, 0)
        time.sleep(a)
        self.brower.FindClasses("J_input_fz")[2].send_keys(".")
        self.brower.FindClasses("J_input_fz")[2].send_keys("150")
        self.brower.FindClasses("J_input_fz")[2].send_keys("10")
        time.sleep(a)

    # 填写分值 简答题
    try:
        self.brower.FindClasses("J_input_fz")[3].send_keys("10")
        time.sleep(a)
    except ElementNotVisibleException as e:
        win32api.keybd_event(34, 0, 0, 0)
        time.sleep(a)
        self.brower.FindClasses("J_input_fz")[3].send_keys("10")
        time.sleep(a)

    # 点击查看答案解析
    self.brower.FindLink_text("查看答案解析").click()
    time.sleep(a)
    # 点击隐藏答案解析
    self.brower.FindLink_text("隐藏答案解析").click()
    time.sleep(a)

    # 将屏幕重新定位到顶部，这样才能确保找到第一道题
    win32api.keybd_event(172, 0, 0, 0)
    time.sleep(a)
    # 上移 第一道题上移 提示
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[2]/div[2]/div[1]/div[3]/p/a[2]").click()
    time.sleep(a)
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"已经是第一道试题！")
    time.sleep(a)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(a)

    # 将屏幕重新定位到底部，这样能确保不是第一道题
    win32api.keybd_event(35, 0, 0, 0)
    time.sleep(a)

    # 上移  不是第一道题
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[2]/div[2]/div[2]/div[3]/p/a[2]").click()
    time.sleep(b)
    time.sleep(b)

    # 下移  最后一道题下移 提示
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[2]/div[2]/div[2]/div[3]/p/a[3]").click()
    time.sleep(a)
    # 断言提示
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"已经是最后一道试题！")
    time.sleep(a)
    # 关闭弹框
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(a)

    # 将屏幕重新定位到顶部，这样才能确保找到最后一道题
    win32api.keybd_event(172, 0, 0, 0)
    time.sleep(a)

    # 下移 不是最后一道题
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[2]/div[2]/div[1]/div[3]/p/a[3]").click()
    time.sleep(a)
    # 点击删除
    self.brower.FindXpath("//*[@id='zujuan_content']/div[1]/div[2]/div[2]/li[2]/div[2]/div[1]/div[3]/p/a[4]").click()
    time.sleep(a)
    time.sleep(a)


