#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:38:59
@LastEditTime: 2019-02-28 20:40:52
'''


def countsequence():
    a = 2.0
    b = 1.0
    s = 0
    for n in range(1, 21):
        s += a/b
        t = a
        a = a + b
        b = t
    print(s)
    return


countsequence()
