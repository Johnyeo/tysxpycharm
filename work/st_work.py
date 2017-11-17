# -*- coding:utf-8 -*-
import time
# 试题作业
from util import st_work,save_work,cancle_st_work
from util import insert_st_work
# 布置作业
from  util import bz_work_class,bz_work_group,bz_work_students

def STWork(self):
    # 发布试题作业
    # 保存试题
    save_work.save_st_Work(self)
    # 添加作业
    insert_st_work.Insert_st_Work(self)
    # 点击布置作业
    # 按小组布置
    self.brower.FindClasses("J_btn_bz")[0].click()
    time.sleep(3)
    # 点击确定
    self.brower.FindId("prompt-wd_prompt_close-ok-confirm").click()
    time.sleep(3)
    bz_work_group.bz_work_Group(self)


        # # 放弃编辑 不保存试题作业
        # cancle_st_work.cancle_st_Work(self)
