#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 21:32:22
@LastEditTime: 2019-02-27 21:45:22
'''


def tabletennismatch():
    Msg = 'Well Done!'
    for i in range(ord('x'), ord('z') + 1):
        for j in range(ord('x'), ord('z') + 1):
            if i != j:
                for k in range(ord('x'), ord('z') + 1):
                    if (i != k) and (j != k):
                        if(i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                            print('order is a -- {}\t b -- {}\t c--{}'.format(chr(i), chr(j), chr(k)))
    return Msg


print(tabletennismatch())
