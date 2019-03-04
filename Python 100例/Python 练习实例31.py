#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-04 19:36:50
@LastEditTime: 2019-03-04 19:50:53
'''
letter = input('please input:')
# while letter != 'Y':
if letter == 'S':
    print('please input second letter:')
    letter = input('please input:')
    if letter =='a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('data error')

elif letter == 'F':
    print('Friday')

elif letter == 'M':
    print('Monday')

elif letter == 'T':
    print('pleaase input second letter')
    letter = input('please input:')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data error')
elif letter == 'W':
    print('Wednesday')
else:
    print('data error')
