#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:58:12
@LastEditTime: 2019-02-28 21:00:34
'''


def countwithrecursive(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * countwithrecursive(j - 1)
    return sum


print(countwithrecursive(5))
