# -*- coding:utf-8 -*-
import unittest
from util import unittestutil, urlutil, loginutil
from util import bz_work_class, bz_work_group, bz_work_students
# 发布文件作业
from work import file_work
# 发布试题作业
from work import st_work
# 最新作业
from work import news_work
# 全部作业
from work import all_work
# 本校共享作业
from work import share_work

import time


class TYSXwork(unittest.TestCase):
    # 测试用例没执行之前执行此方法
    @classmethod
    def setUpClass(self):
        # 初始化浏览器类对象
        self.brower = unittestutil.Chrome()
        pass

    # 测试用例每执行一条前执行此方法
    def setUp(self):
        # 打开浏览器
        self.brower.StartChrom(urlutil.URL.TYSX_WORK)
        pass

    # 所以测试用例执行完后执行此方法
    @classmethod
    def tearDownClass(self):
        pass

    # 测试用例执行完一条后执行此方法
    def tearDown(self):
        # 关闭浏览器
        self.brower.CloseChrom()
        pass

    # 测试用例
    # 发布自动化文件作业
    def test_a_fa_file_work(self):
        # 登录成功
        loginutil.login(self)
        time.sleep(3)
        # 切换作业管理页面
        self.brower.FindId("zygl").click()
        time.sleep(3)
        # 发布文件作业
        file_work.FileWork(self)

    # 发布自动化试题作业
    def test_b_fa_sc_work(self):
        # 登录成功
        loginutil.login(self)
        time.sleep(3)
        # 切换作业管理页面
        self.brower.FindId("zygl").click()
        time.sleep(3)
        # 发布试题作业
        st_work.STWork(self)

    # 全部作业
    def test_c_all_work(self):
        # 登录成功
        loginutil.login(self)
        time.sleep(3)
        # 切换作业管理页面
        self.brower.FindId("zygl").click()
        time.sleep(3)
        # 最新作业
        news_work.NewsWokd(self)
        # 全部作业
        all_work.AllWork(self)
        # 本校共享作业
        share_work.ShareWork(self)
