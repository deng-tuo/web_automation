#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner
import time
import os
from test_case.test_interface import TestInterface

root_dir = os.path.dirname(os.path.abspath('.'))
path = root_dir + r'\huanbao\report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
HtmlFile = path + now + r"Test_report.html"
fp = open(HtmlFile, 'wb',)

suite = unittest.TestLoader().discover("test_case")
# 运行test_case文件下的全部用例

# suite = unittest.TestSuite(unittest.makeSuite(TestInterface)) 运行一个类里面的用例

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title = "测试报告",
                                           description = "测试情况",
                                           verbosity = 2)
runner.run(suite)
fp.close()


