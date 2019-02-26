#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-26 20:59:58
@LastEditTime: 2019-02-26 21:22:53
'''


def countdaffodilnumber():
    list = []
    for n in range(100, 1000):
        i = int(n / 100)
        j = int(n / 10 % 10)
        k = int(n % 10)
        if n == i ** 3 + j ** 3 + k ** 3:
            list.append(n)
    return list


# countdaffodilnumber()

print(countdaffodilnumber())
