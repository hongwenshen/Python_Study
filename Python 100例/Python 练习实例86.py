#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-20 20:03:44
@LastEditTime: 2019-03-20 20:05:46
'''
'''
题目：两个字符串连接程序。
'''

if __name__ == '__main__':
    a = 'acegikm'
    b = 'bdfhjlnpq'
    # 连接字符串
    c = a + b
    d = ''
    print(c)
    print(d.join([a, b]))
