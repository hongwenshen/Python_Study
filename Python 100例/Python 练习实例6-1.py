#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 20:45:28
@LastEditTime: 2019-02-25 20:48:06
'''


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a+b
    return a


# 输出了第10个斐波那契数列
print(fib(10))
