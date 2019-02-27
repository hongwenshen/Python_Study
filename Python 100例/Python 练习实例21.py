#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 21:30:04
@LastEditTime: 2019-02-27 21:31:53
'''


def monkeyeatingpeach():
    x2 = 1
    for day in range(9, 0, -1):
        x1 = (x2 + 1) * 2
        x2 = x1
    print(x1)
    return x1


print(monkeyeatingpeach())
