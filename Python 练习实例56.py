#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-12 21:03:55
@LastEditTime: 2019-03-12 21:10:14
'''
'''
题目：画图，学用circle画圆形。　
'''

if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas(width = 800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1.0
    j = 1.0
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width = 1)
        k += j
        j += 0.3
    
    mainloop()
