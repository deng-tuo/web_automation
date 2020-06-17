#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from config.read_ini import read_ini
import time

class InitWeb(object):

    def __init__(self, driver):
        self.driver = driver

    def initWeb(self):
        self.driver = webdriver.Chrome()
        url = read_ini("parameter", "url")
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

        account_element = read_ini("Element", "account_element")
        password_element = read_ini("Element", "password_element")
        login_element = read_ini("Element", "login_element")
        account = read_ini("parameter", "account_name")
        password = read_ini("parameter", "password_name")

        self.driver.find_element_by_id(account_element).send_keys(account)
        self.driver.find_element_by_id(password_element).send_keys(password)
        self.driver.find_element_by_id(login_element).click()
        self.driver.implicitly_wait(6)
        return self.driver

    def quitWeb(self):
        self.driver.quit()

if __name__ == "__main__":
    open = InitWeb(object)
    open.initWeb()

