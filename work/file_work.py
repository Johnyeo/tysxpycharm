# -*- coding:utf-8 -*-
# 文件作业
from util import news_file_work,cancle_file_work
# 布置作业
from  util import bz_work_class,bz_work_group,bz_work_students
from util import save_work
import time
def FileWork(self):
    # 发布文件作业
    # 保存作业
    #save_work.SaveFileWork(self)
    # 布置作业
    news_file_work.NewsWork(self)
    # 点击布置按钮
    self.brower.FindId("J_btn_bz").click()
    time.sleep(3)
    # 按班级布置
    bz_work_class.bz_work_Class(self)


