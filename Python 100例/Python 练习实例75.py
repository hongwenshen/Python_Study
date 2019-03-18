#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-18 21:06:24
@LastEditTime: 2019-03-18 21:08:05
'''
'''
题目：放松一下，算一道简单的题目。
'''

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1:
            n += 1
        if i == 3:
            n += 1
        if i == 4:
            n += 1
        if i != 4:
            n += 1
        if n == 3:
            print(64 + i)
