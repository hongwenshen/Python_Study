#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:42:57
@LastEditTime: 2019-02-28 20:50:34
'''
from functools import reduce


def countsequnce():
    a = 2
    b = 1
    sum = []
    sum.append(a / b)
    for n in range(1, 20):
        b, a = a, a+b
        sum.append(a / b)
    print(reduce(lambda x, y: x + y, sum))
    return


countsequnce()
