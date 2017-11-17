# -*- coding:utf-8 -*-
import time
import st_work
def cancle_st_Work(self):
    st_work.stWork(self)
    self.brower.FindClasses("J_btn_fqbj")[0].click()
    time.sleep(3)
    self.assertEqual(self.brower.FindId("prompt-text-confirm").text,u"作业还没有保存，确定放弃编辑？")
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    # 断言
    self.assertEqual(self.brower.driver.title,u"作业管理")
