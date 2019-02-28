#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 21:01:03
@LastEditTime: 2019-02-28 21:03:41
'''


def output(s, length):
    if length == 0:
        return
    print(s[length-1])
    output(s, length-1)


s = input('Input a string:')
length = len(s)
output(s, length)
