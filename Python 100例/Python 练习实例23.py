#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-28 20:33:52
@LastEditTime: 2019-02-28 20:38:36
'''
from sys import stdout


def printdiamond():
    for i in range(4):
        for j in range(2 - i + 1):
            stdout.write(' ')
        for k in range(2 * i + 1):
            stdout.write('*')
        print()
    for i in range(3):
        for j in range(i + 1):
            stdout.write(' ')
        for k in range(4 - 2*i + 1):
            stdout.write('*')
        print()
    return


printdiamond()
