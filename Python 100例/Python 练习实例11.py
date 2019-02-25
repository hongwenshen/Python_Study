#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 21:34:07
@LastEditTime: 2019-02-25 21:38:45
'''


def rabbit():
    f1 = 1
    f2 = 1
    for i in range(1, 22):
        print('%12ld %12ld' % (f1, f2))
        if