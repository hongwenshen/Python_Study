#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-18 21:02:52
@LastEditTime: 2019-03-18 21:04:48
'''
'''
题目：列表排序及连接。

程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
'''

if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    a.sort()  # 对列表a进行排序
    print(a)
    # 连接列表a与b
    print(a+b)
    # 连接列表a与b
    a.extend(b)
    print(a)
