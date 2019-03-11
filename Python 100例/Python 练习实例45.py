#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:35:15
@LastEditTime: 2019-03-11 21:37:08
'''
'''
题目：统计 1 到 100 之和。
'''


def countfromzerotohundrend():
    temp = 0
    for i in range(1, 101):
        temp += i
    print('The sum is {}'.format(temp))
    return temp


countfromzerotohundrend()
