#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-12 20:47:36
@LastEditTime: 2019-03-12 20:49:03
'''
'''
题目：学习使用按位异或 ^ 。

程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
'''

if __name__ == '__main__':
    a = 0o77
    b = a ^ 3
    print('The a ^ 3 = {:d}'.format(b))
    b ^= 7
    print('The a ^ b = {:d}'.format(b))
