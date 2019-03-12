#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-12 20:32:34
@LastEditTime: 2019-03-12 20:36:26
'''
'''
题目：使用lambda来创建匿名函数。
'''

MAXIMUM = lambda x, y : (x > y) * x + (x < y) * y
MINIMUM = lambda x, y : (x > y) * y + (x < y ) * x


if __name__ == '__main__':
    a = 10
    b = 20
    print('The larger one is {0:d}'.format(MAXIMUM(a, b)))
    print('The lower one is {0:d}'.format(MINIMUM(a, b)))
