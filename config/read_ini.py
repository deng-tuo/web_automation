#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os

# class ReadIni(object):

def read_ini(ini_class, ini_name):
    file_path = os.path.dirname(os.path.abspath(__file__)) + r'\config_ini.ini'
    # file_path = r"G:\huanbao\config\config_ini.ini"
    cfg = configparser.ConfigParser()
    cfg.read(file_path, encoding='UTF-8')
    cf = cfg.get(ini_class, ini_name)
    return cf

if __name__ == "__main__":
    print(read_ini("parameter", "url"))
