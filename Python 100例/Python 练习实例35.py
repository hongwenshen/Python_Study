#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-04 20:09:53
@LastEditTime: 2019-03-04 20:20:03
'''


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARNING + "警告的颜色字体？" + bcolors.ENDC)
print(bcolors.OKGREEN + "警告的颜色字体？" + bcolors.ENDC)
print(bcolors.HEADER + "警告的颜色字体？" + bcolors.ENDC)
print(bcolors.OKBLUE + "警告的颜色字体？" + bcolors.ENDC)
print(bcolors.BOLD + "警告的颜色字体？" + bcolors.ENDC)
