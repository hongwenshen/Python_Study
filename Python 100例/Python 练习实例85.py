#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-20 19:57:10
@LastEditTime: 2019-03-20 20:02:53
'''
'''
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

程序分析：999999 / 13 = 76923。
'''
if __name__ == '__main__':
    zi = int(input('输入一个数字：\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print('{0:d}个9可以被{1:d}整除：{2:d}'.format(c9, zi, sum))
    r = sum // zi
    print('{0:d} / {1:d} = {2:d}'.format(sum, zi, r))
