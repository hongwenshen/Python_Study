#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-26 21:23:18
@LastEditTime: 2019-02-26 21:46:24
'''


def reduceNum(n):
    print('{0:2d} = '.format(n), end='\t')
    list = []
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字')
        exit(0)
    elif n in [1]:
        print('{0:2d}'.format(n), end='\t'),
    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index  # n 等于 n // index
                if n == 1:
                    list.append(index)
                    print('{0:2d}'.format(index), end='\t')
                else:  # index 一定是素数
                    list.append(index)
                    print('{0:2d} *'.format(index), end='\t')
                break
    return list


print(reduceNum(90))
print(reduceNum(100))
