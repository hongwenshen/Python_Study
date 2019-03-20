#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-20 20:06:04
@LastEditTime: 2019-03-20 20:09:23
'''
'''
题目：回答结果（结构体变量传递）。
'''

if __name__ == '__main__':
    class student:
        x = 0
        c = 0

    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a = student()
    a.x = 3
    a.c = 'a'
    print(a.x, a.c)
    f(a)
    print(a.x, a.c)
