#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-20 19:50:46
@LastEditTime: 2019-03-20 19:53:02
'''
'''
题目：求0—7所能组成的奇数个数。

程序分析：

组成1位数是4个。

组成2位数是7*4个。

组成3位数是7*8*4个。

组成4位数是7*8*8*4个。
'''

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2, 9):
        print(sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print('sum = {:d}'.format(sum))
