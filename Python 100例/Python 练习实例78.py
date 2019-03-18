#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-18 21:21:20
@LastEditTime: 2019-03-18 21:24:19
'''
'''
题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
'''

if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    print('{:s},{:d}'.format(m, person[m]))
