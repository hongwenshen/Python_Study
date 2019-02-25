#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 21:34:07
@LastEditTime: 2019-02-25 21:55:31
'''


def rabbit():
    Msg = "Well done"
    f1 = 1
    f2 = 1
    for i in range(1, 22):
        print('{0:12d} {1:12d}'.format(f1, f2), end='\t')
        if (i % 3) == 0:
            print('') 
        f1 = f1 + f2
        f2 = f1 + f2
    return Msg


print(rabbit())
