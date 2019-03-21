#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-21 20:31:40
@LastEditTime: 2019-03-21 20:37:26
'''
'''
题目：时间函数举例3。
'''
if __name__ == '__main__':
    import time
    start = time.process_time()
    start1 = time.perf_counter()
    for i in range(10000):
        print(i)
    end = time.process_time()
    end1 = time.perf_counter()
    print('different is {:6.3f}'.format(end - start))
    print('different is {:6.3f}'.format(end1 - start1))
