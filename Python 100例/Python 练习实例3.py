#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-24 21:25:11
@LastEditTime: 2019-02-24 21:34:10
'''
for i in range(1, 85):
    if 168 % i == 0:
        j = 168/i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(m, n, x)
