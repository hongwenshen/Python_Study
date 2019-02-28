#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 21:04:48
@LastEditTime: 2019-02-28 21:05:38
'''


def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c


print(age(5))
