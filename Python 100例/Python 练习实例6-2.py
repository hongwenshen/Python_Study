#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 20:48:28
@LastEditTime: 2019-02-25 20:51:40
'''


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# 输出了第10个斐波那契数列
print(fib(10))
