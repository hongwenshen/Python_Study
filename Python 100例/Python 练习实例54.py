#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-12 20:50:17
@LastEditTime: 2019-03-12 20:55:12
'''
'''
题目：取一个整数a从右端开始的4〜7位。

程序分析：可以这样考虑： 
(1)先使a右移4位。 
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
(3)将上面二者进行&运算。
'''
'''
1. 取反 ~0 = 11111111 11111111 11111111 11111111
2. 左移 ~0 << 4 = 11111111 11111111 11111111 11110000
3.取反 ~(~0<<4) = 00000000 00000000 00000000 00001111
'''

if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print('{0:o}\t{1:o}'.format(a, d))
