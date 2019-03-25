#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-25 21:55:56
@LastEditTime: 2019-03-25 21:58:27
'''
'''
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
'''
if __name__ == "__main__":
    fp = open('test.txt', 'w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt', 'r')
    print(fp.read())
    fp.close()
