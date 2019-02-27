#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 20:46:35
@LastEditTime: 2019-02-27 20:56:56
'''


# 使用while实现
def countstring():
    Msg = "Well Done!"
    s = input('请输入一个字符串:\n')
    lettes = 0
    space = 0
    digit = 0
    others = 0
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        if c.isalpha():
            lettes += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char ={}, space ={}, dight ={}, others ={}'.format(lettes, space, digit, others))
    return Msg


print(countstring())
