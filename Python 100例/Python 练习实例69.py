#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-17 21:44:56
@LastEditTime: 2019-03-17 22:01:44
'''
'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''

if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i+1)
    i = 0
    k = 0
    m = 0
    while m < n-1:  # 当退出人数比n-1少时（即未退出人数大于1时）执行循环体
        if num[i] != 0:
            k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n:
            i = 0
    i = 0
    while num[i] == 0:
        i += 1
    print(num[i])
