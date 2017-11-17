# -*- coding:utf-8 -8-
import time
def pyFileWork(self):
    # 有待批作业 点击待批作业按钮  批改文件作业
    self.brower.FindLink_text("待批改(1)").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.driver.title,u"批阅文件作业")
    time.sleep(3)
    # 点击批改
    self.brower.FindLink_text("批改").click()
    time.sleep(3)
    # 点击勾选正确
    self.brower.FindXpath("//*[@id='dui']").click()
    time.sleep(3)
    # 将对勾放在图片上
    self.brower.FindId("canvas").click()
    time.sleep(3)
    # 点击保存图标
    self.brower.FindId("imgurl").click()
    time.sleep(3)
    # 输入分值 分值超过本题的分值
    self.brower.FindXpath("//*[@id='pyzy_wj_zylb']/div[1]/div[3]/div[1]/ul/li/span/input").send_keys(50)
    time.sleep(3)
    # 点击对勾图标
    self.brower.FindXpath("//*[@id='pyzy_wj_zylb']/div[1]/div[3]/div[1]/ul/li/i[1]").click()
    time.sleep(3)
    # 点击完成批阅
    self.brower.FindClasses("J_btn_wcpf")[0].click()
    time.sleep(3)
    # # 断言
    # self.assertEqual(self.brower.FindId("prompt-text-alert").text,u"得分不能超过作业总分，总分为30分!")
    # time.sleep(3)
    # 点击关闭按钮
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(3)
    # 清除错误分值
    self.brower.FindXpath("//*[@id='pyzy_wj_zylb']/div[1]/div[3]/div[1]/ul/li/span/input").clear()
    time.sleep(3)
    # 输入分值 分值等于本题的分值
    self.brower.FindXpath("//*[@id='pyzy_wj_zylb']/div[1]/div[3]/div[1]/ul/li/span/input").send_keys(30)
    time.sleep(3)
    # 点击完成批阅
    self.brower.FindClasses("J_btn_wcpf")[0].click()
    time.sleep(3)
    # 成功跳转到上一页面
    # 断言
    self.assertEqual(self.brower.driver.title,u"作业管理")
    time.sleep(3)

def pyStWork(self):
    # 批阅作业--试题作业
    # 点击批阅作业
    self.brower.FindLink_text("待批改(1)").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.driver.title, u"批阅试题作业")
    time.sleep(3)
    # 查看题目
    self.brower.FindClasses("J_btn_cktm")[0].click()
    time.sleep(3)
    # 查看答案解析
    self.brower.FindId("ckda").click()
    time.sleep(3)
    # 隐藏答案解析
    self.brower.FindId("ckda").click()
    time.sleep(3)
    # 点击退出题目
    self.brower.FindClass("close").click()
    time.sleep(3)
    # 点击批改
    self.brower.FindClasses("opencanvans")[0].click()
    time.sleep(3)
    # 进入图片批改页面
    # 点击半对图标
    self.brower.FindId("bandui").click()
    time.sleep(3)
    # 将图标放在图片上
    self.brower.FindId("canvas").click()
    time.sleep(3)
    # 对图片批改有错误  可以对其内容清除
    # 点击清除图标
    self.brower.FindId("clear").click()
    time.sleep(3)
    # 弹框确认是否要清除全部内容
    self.assertEqual(self.brower.FindXpath("//*[@id='sure']/p").text, u"是否要清除全部批改内容及操作")
    # 如果是的话点击确定
    self.brower.FindId("clearall").click()
    time.sleep(3)
    # 再做出正确的批改
    # 点击错误图标
    self.brower.FindId("cuo").click()
    time.sleep(3)
    # 将图标放在图片上
    self.brower.FindId("canvas").click()
    time.sleep(3)
    # 点击保存图标
    self.brower.FindId("imgurl").click()
    time.sleep(3)
    # 没有打分 没有选择对错的情况下点击完成批阅
    self.brower.FindClasses("J_btn_wcpf")[0].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"请打分!")
    time.sleep(3)
    # 点击关闭
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(3)
    # 输入分值
    self.brower.FindClasses("J_zf")[0].send_keys("30")
    time.sleep(3)
    # 点击完成批阅
    self.brower.FindClasses("J_btn_wcpf")[0].click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-alert").text, u"请判断学生答案对错!")
    time.sleep(3)
    # 点击关闭
    self.brower.FindId("prompt-wd_prompt_close-alert").click()
    time.sleep(3)
    # 点击错误图标
    self.brower.FindXpath("//*[@id='AnswerBox']/div/div[2]/p/i[2]").click()
    time.sleep(3)
    # 点击完成批阅
    self.brower.FindClasses("J_btn_wcpf")[0].click()
    time.sleep(3)