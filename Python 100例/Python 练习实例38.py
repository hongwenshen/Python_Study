#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-04 20:48:58
@LastEditTime: 2019-03-04 20:51:40
'''


if __name__ == "__main__":
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input('input num:\n')))
    for i in range(3):
        sum += a[i][i]
    print(sum)
