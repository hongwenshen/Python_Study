#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-18 20:42:04
@LastEditTime: 2019-03-18 21:35:48
'''
'''
题目：编写input()和output()函数输入，输出5个学生的数据记录。
'''

N = 3
# stu
# num : string
# name : string
# score[4] : list
student = []
for i in range(5):
    student.append(['', '', []])


def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('scores:\n')))


def output_stu(stu):
    for i in range(N):
        print('{0:<6s}{1:<10s}'.format(stu[i][0], stu[i][1]))
        for j in range(3):
            print('{:<8d}'.format(stu[i][2][j]))


if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)
