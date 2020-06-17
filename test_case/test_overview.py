#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from init_web import InitWeb
from config.read_ini import read_ini

class TestInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.init = InitWeb(self)
        self.driver = self.init.initWeb()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_big_data_001(self):
        # w内置iframe的用法
        self.driver.switch_to_frame('first')
        all_sum_element = read_ini("Element", "all_sum")
        self.driver.find_element_by_id(all_sum_element).click()
        self.driver.implicitly_wait(5)

    def test_big_data_002(self):
        # 接着big_data_001继续操作iframe里的弹窗界面
        all_sum_02_element = read_ini("Element", "all_sum_02")
        self.driver.find_element_by_xpath(all_sum_02_element).click()
        self.driver.implicitly_wait(5)

if __name__ == "__main__":
    unittest.main()