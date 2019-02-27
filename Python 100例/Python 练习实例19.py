#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 21:09:21
@LastEditTime: 2019-02-27 21:15:13
'''
from sys import stdout


def countcompletenumbers():
    Msg = 'Well Done!'
    for j in range(2, 1001):
        k = []
        n = -1
        s = j
        for i in range(1, j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
        if s == 0:
            print(j)
            for i in range(n):
                stdout.write(str(k[i]))
                stdout.write('')
            print(k[n])
    return Msg


print(countcompletenumbers())
