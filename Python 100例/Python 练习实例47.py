#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:41:26
@LastEditTime: 2019-03-11 21:44:47
'''
'''
题目：两个变量值互换。
'''


def exchange(a, b):
    a, b = b, a
    return(a, b)


if __name__ == '__main__':
    x = 10
    y = 20
    print('x = {0:d}, y= {0:d}'.format(x, y))
    x, y = exchange(x, y)
    print('x = {0:d}, y= {0:d}'.format(x, y))
