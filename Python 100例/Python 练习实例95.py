#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-21 20:50:43
@LastEditTime: 2019-03-21 20:56:33
'''
'''

题目：字符串日期转换为易读的日期格式。
'''
if __name__ == "__main__":
    from dateutil import parser
    dt = parser.parse("Mar 21 20:56:30 UTC 2019")
    print(dt)
