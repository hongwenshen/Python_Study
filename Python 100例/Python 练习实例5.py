#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-24 21:53:05
@LastEditTime: 2019-02-24 21:55:14
'''

line = []
for i in range(3):
    x = int(input('integer:\n'))
    line.append(x)
line.sort()
print(line)