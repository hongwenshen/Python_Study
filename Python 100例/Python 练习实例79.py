#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-18 21:25:44
@LastEditTime: 2019-03-18 21:28:18
'''
'''
题目：字符串排序。
'''

if __name__ == '__main__':
    str1 = input('input string:\n')
    str2 = input('input string:\n')
    str3 = input('input string:\n')
    print(str1, str2, str3)
    if str1 > str2:
        str1, str2 = str2, str1
    if str1 > str3:
        str1, str3 = str3, str1
    if str2 > str3:
        str2, str3 = str3, str2
    print('after being sorted.')
    print(str1, str2, str3)
