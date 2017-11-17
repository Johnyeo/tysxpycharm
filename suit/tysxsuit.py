# -*- coding:utf-8 -*-
import os
import unittest
from tysxunittest import tysxlogin
from tysxunittest import tysxwork
import HTMLTestRunner
# 设置系统的编码格式为utf-8 设置下面这三句的目的是为了在自动化测试报告断言出错的时候能看中文
# import sys
# # 重载sys
# reload(sys)
# # 设置编码格式
# sys.setdefaultencoding("utf-8")


# 初始化suit
suit=unittest.TestSuite()
# 添加测试套件
#suit.addTest(unittest.makeSuite(tysxlogin.TYSX))
suit.addTest(unittest.makeSuite(tysxwork.TYSXwork))

# 设置自动化测试报告的路径
# fileUrl="D:/HtmlTestRunner/tysx.html"

# 报告路径在当前目录下
fileUrl=os.getcwd()+'\\tysx.html'

# 以IO流的形式写入
fl=file(fileUrl,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fl,title=u"天元数学网",description=u"详情界面")
runner.run(suit)





