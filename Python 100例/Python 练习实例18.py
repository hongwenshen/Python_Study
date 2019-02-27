#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 21:02:51
@LastEditTime: 2019-02-27 21:08:06
'''
from functools import reduce


def countvalues():
    Msg = 'Well Done!'
    Tn = 0
    Sn = []
    n = int(input('n = '))
    a = int(input('a = '))
    for count in range(n):
        Tn = Tn + a
        a = a * 10
        Sn.append(Tn)
        print(Tn)
    Sn = reduce(lambda x, y: x + y, Sn)
    print('计算和为：{}'.format(Sn))
    return Msg


print(countvalues())
