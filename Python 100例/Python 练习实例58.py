#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-16 10:24:22
@LastEditTime: 2019-03-16 10:33:49
'''
'''
题目：画图，学用rectangle画方形。　　　
'''
from tkinter import *
if __name__ == '__main__':
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=400, height=400, bg='yellow')
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
    canvas.pack()
    root.mainloop()
