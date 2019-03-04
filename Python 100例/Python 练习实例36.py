#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-04 20:20:26
@LastEditTime: 2019-03-04 20:30:12
'''
# 输出指定范围内的素数


def countprimenumber(x, y):
    line = []
    for num in range(x, y):
        # 素数大于1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    line.append(num)
                    print(num)
    return line


# 用户输入数据
lower = int(input('请输入区间的最小值：'))
upper = int(input('请输入区间的最大值：'))

countprimenumber(lower, upper)
