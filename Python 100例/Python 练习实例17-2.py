#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 20:57:18
@LastEditTime: 2019-02-27 21:01:31
'''


def countstringusefor():
    Msg = 'Well Done!'
    s = input('请输入一个字符串：\n')
    letters = 0
    space = 0
    digit = 0
    others = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char = {}, space = {}, digit = {}, others = {}'.format(letters, space, digit, others))
    return Msg


print(countstringusefor())
