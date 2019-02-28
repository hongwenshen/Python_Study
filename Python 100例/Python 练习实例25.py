#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:51:05
@LastEditTime: 2019-02-28 20:52:57
'''


def tired():
    n = 0
    s = 0
    t = 1
    for n in range(1, 21):
        t *= n
        s += t
    print('结果是{}'.format(s))
    return


tired()
