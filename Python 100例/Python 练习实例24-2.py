#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:41:24
@LastEditTime: 2019-02-28 20:42:36
'''


def countsequences():
    a = 2.0
    b = 1.0
    s = 0.0
    for n in range(1, 21):
        s += a / b
        b, a = a, a+b
    print(s)
    return


countsequences()
