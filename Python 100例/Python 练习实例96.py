#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-21 20:57:25
@LastEditTime: 2019-03-21 20:58:48
'''
'''
题目：计算字符串中子串出现的次数。
'''

if __name__ == "__main__":
    str1 = input('请输入一个字符串：\n')
    str2 = input('请输入一个子字符串：\n')
    ncount = str1.count(str2)
    print(ncount)
