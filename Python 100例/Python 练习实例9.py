#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-25 21:21:56
@LastEditTime: 2019-02-25 21:26:46
'''
import time


def pauseonesec():
    Msg = "Well done"
    myD = {1: 'a', 2: 'b'}
    for key, value in dict.items(myD):
        print(key, value)
        time.sleep(1)
    return Msg


print(pauseonesec())

# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print(key, value)
#     time.sleep(1)
