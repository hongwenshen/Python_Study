#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-17 21:36:15
@LastEditTime: 2019-03-17 21:42:15
'''
'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

if __name__ == '__main__':
    n = int(input('整数n为：\n'))
    m = int(input('向后移m个位置\n'))

    def move(array, n, m):
        array_end = array[n-1]
        for i in range(n-1, -1, -1):
            array[i] = array[i-1]
        array[0] = array_end
        m -= 1
        if m > 0:
            move(array, n, m)
    number = []
    for i in range(n):
        number.append(int(input('输入一个数字：\n')))
    print('原始列表：{}'.format(number))

    move(number, n, m)

    print('移动之后：{}'.format(number))
