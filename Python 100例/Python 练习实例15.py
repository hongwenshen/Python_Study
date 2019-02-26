#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-26 21:47:04
@LastEditTime: 2019-02-26 21:59:49
'''


def scores():
    score = int(input('输入分数：\n'))
    Msg = "Well Done!"
    if score >= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    else:
        grade = 'C'
    print('{0:d} 属于 {1:s}'.format(score, grade), end='\t')
    return Msg


scores()
