#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-26 20:48:52
@LastEditTime: 2019-02-26 20:59:14
'''
from math import sqrt


def countprimenumber():
    msg = 'Well done!'
    h = 0
    leap = 1
    for m in range(101, 201):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print("{0:4d}".format(m))
            h += 1
            if h % 10 == 0:
                print('\t')
        leap = 1
    print('The total is {0:4d}'.format(h))
    return msg


print(countprimenumber())
