#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-20 20:09:45
@LastEditTime: 2019-03-20 20:12:48
'''
'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''

if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(input('input a number:\n'))
        print(a * '*')
        n += 1
