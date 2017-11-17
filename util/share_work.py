# -*- coding:utf-8 -*-
import time
def AllWork_ShreWorkS(self):
    # 点击共享作业 有学校的老师
    self.brower.FindLink_text("共享").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"作业共享后将共享给本校其他老师！")
    time.sleep(3)
    # 点击确定 共享成功
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    # 切换本校共享作业页面 可查看
    self.brower.FindId("J_tab_bxgxzy").click()
    time.sleep(3)
    # 切换最新作业页面
    self.brower.FindId("J_tab_zxzy").click()



def AllWork_ShreWorkNoS(self):
    # 点击共享作业  没有学校的老师
    self.brower.FindLink_text("共享").click()
    time.sleep(3)
    # 弹出填写学校页面
    # 选择山东省学校
    self.brower.FindXpath("//*[@id='1100000000000001000']").click()
    time.sleep(3)
    # 选择青岛市教育局
    self.brower.FindLink_text("青岛市教育体育局").click()
    time.sleep(3)
    # 选择市北区教育体育局
    self.brower.FindLink_text("市北区教育体育局").click()
    time.sleep(3)
    # 选择 青岛第四十三中学
    self.brower.FindLink_text("青岛第四十三中学").click()
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-edit-prompt_wsxxxx").click()


def NewWork_ShareWorkS(self):
    # 点击共享作业 有学校的老师
    self.brower.FindLink_text("共享作业").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"作业共享后将共享给本校其他老师！")
    time.sleep(3)
    # 点击确定 共享成功
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    # 切换本校共享作业页面 可查看
    self.brower.FindId("J_tab_bxgxzy").click()
    time.sleep(3)
    # 切换最新作业页面
    self.brower.FindId("J_tab_zxzy").click()


def NewWork_ShreWorkNoS(self):
    # 点击共享作业  没有学校的老师
    self.brower.FindLink_text("共享作业").click()
    time.sleep(3)
    # 弹出填写学校页面
    # 选择山东省学校
    self.brower.FindXpath("//*[@id='1100000000000001000']").click()
    time.sleep(3)
    # 选择青岛市教育局
    self.brower.FindLink_text("青岛市教育体育局").click()
    time.sleep(3)
    # 选择市北区教育体育局
    self.brower.FindLink_text("市北区教育体育局").click()
    time.sleep(3)
    # 选择 青岛第四十三中学
    self.brower.FindLink_text("青岛第四十三中学").click()
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-edit-prompt_wsxxxx").click()
