#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:29:44
@LastEditTime: 2019-03-11 21:34:12
'''
'''
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
'''

x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 迭代输出行
for i in range(len(x)):
    # 迭代输出列
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)
