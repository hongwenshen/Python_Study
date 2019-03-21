#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-21 20:27:23
@LastEditTime: 2019-03-21 20:29:07
'''
'''
题目：时间函数举例1。
'''
if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime()))
    print(time.asctime(time.gmtime(time.time())))
