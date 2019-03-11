#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:20:34
@LastEditTime: 2019-03-11 21:22:52
'''


'''
题目：学习使用auto定义变量的用法。

程序分析：没有auto关键字，使用变量作用域来举例吧。
'''
num = 2


def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1


for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()
