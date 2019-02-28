#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:53:15
@LastEditTime: 2019-02-28 20:57:41
'''
s = 0
list = range(1, 21)


def op(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r


'''
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
'''

s = sum(map(op, list))
print('结果是{}'.format(s))
