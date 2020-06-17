#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from init_web import InitWeb
from config.read_ini import read_ini
from selenium.webdriver.common.action_chains import ActionChains

class TestInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.init = InitWeb(self)
        self.driver = self.init.initWeb()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_interface_001(self):
        monitoring_element = read_ini("Element", "monitoring_element")
        self.driver.find_element_by_xpath(monitoring_element).click()

    def test_interface_002(self):
        # 鼠标悬停，点击二级菜单
        information_management_element = read_ini("Element", "information_management_element")
        article = self.driver.find_element_by_xpath(information_management_element)
        ActionChains(self.driver).move_to_element(article).perform()
        menu_text_element = read_ini("Element", "menu_text_element")
        self.driver.find_element_by_class_name(menu_text_element).click()

if __name__ == "__main__":
    unittest.main()
