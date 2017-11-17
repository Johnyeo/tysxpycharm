# -*- coding:utf-8 -*-
import time
def CancleShareWork(self):
    # 取消共享
    self.brower.FindLink_text("取消共享").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text, u"确定取消共享？")
    time.sleep(3)
    # 点击确定 取消共享
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)