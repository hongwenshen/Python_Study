#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-21 20:29:55
@LastEditTime: 2019-03-21 20:31:10
'''
'''
题目：时间函数举例2。
'''

if __name__ == '__main__':
    import time
    start = time.time()
    print(start)
    for i in range(3000):
        print(i)
    end = time.time()
    print(end)
    print(end - start)
