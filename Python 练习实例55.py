#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-12 20:56:51
@LastEditTime: 2019-03-12 21:03:21
'''
'''
题目：学习使用按位取反~。

程序分析：~0=1; ~1=0; 
(1)先使a右移4位。 
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
(3)将上面二者进行&运算。
'''
if __name__ == '__main__':
    a = 234
    b = ~a
    print('The a\'s 1 complement is {:d}'.format(b))
    a = ~a
    print('The a\'s 2 complement is {:d}'.format(a))
    