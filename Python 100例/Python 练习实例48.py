#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:45:28
@LastEditTime: 2019-03-11 21:47:22
'''
'''
题目：数字比较。
'''

if __name__ == '__main__':
    i = 10
    j = 20
    if(i > j):
        print('{0:d}大于{1:d}'.format(i, j))
    elif i == j:
        print('{0:d}等于{1:d}'.format(i, j))
    elif i < j:
        print('{0:d}小于{1:d}'.format(i, j))
    else:
        print('未知')
