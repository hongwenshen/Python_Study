#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-19 23:55:31
@LastEditTime: 2019-03-19 23:57:36
'''
'''
题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
求??代表的两位数，及809*??后的结果。
'''

a = 809
for i in range(10, 100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i > 100:
        print(b, ' = 800 *', i, ' + 9 * ', i)
