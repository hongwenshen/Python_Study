#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 21:27:14
@LastEditTime: 2019-02-25 21:33:36
'''
import time


def printpauseonesec():
    Msg = '暂停一秒'
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    return Msg


print(printpauseonesec())
