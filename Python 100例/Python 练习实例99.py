#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-25 21:59:18
@LastEditTime: 2019-03-25 23:37:23
'''
'''
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
if __name__ == "__main__":
    fp = open('test1.txt')
    a = fp.read()
    fp.close()

    fp = open('test2.txt')
    b = fp.read()
    fp.close()

    fp = open('test3.txt', 'w')
    li = list(a + b)
    li.sort()
    s = ''
    s = s.join(li)
    fp.write(s)
    fp.close()
