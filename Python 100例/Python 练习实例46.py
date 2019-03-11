#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:37:40
@LastEditTime: 2019-03-11 21:40:45
'''
'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''
TRUE = 1
FALSE = 0


def SQ(x):
    return x * x


print('如果输入的数字小于50，程序将停止运行。')
again = 1
while again:
    num = int(input('请输入一个数字:'))
    print('运算结果为：{}'.format(SQ(num)))
    if SQ(num) >= 50:
        again = TRUE
    else:
        again = FALSE
