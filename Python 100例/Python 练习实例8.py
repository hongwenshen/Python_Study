#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 20:57:39
@LastEditTime: 2019-02-25 21:21:28
'''


def nineninemultiplicationtable():
    msg = "Well Done"
    for i in range(1, 10):
        for j in range(1, i+1):
            print("{}*{}={} ".format(i, j, i*j), end="\t")
        print()
    return msg


print(nineninemultiplicationtable())

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={} ".format(i, j, i*j), end="\t")
#     print()
