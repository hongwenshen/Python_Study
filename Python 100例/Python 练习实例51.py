#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-12 20:41:47
@LastEditTime: 2019-03-12 20:44:07
'''
'''
题目：学习使用按位与 & 。

程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。
'''

if __name__ == '__main__':
    a = 0o77
    b = a & 3
    print('a & b = {:d}'.format(b))
    b &= 7
    print('a & b = {:d}'.format(b)) 
