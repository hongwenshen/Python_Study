#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-11 21:14:39
@LastEditTime: 2019-03-11 21:18:31
'''


def varfunc():
    var = 0
    print("var = {}".format(var))
    var += 1


if __name__ == '__main__':
    for i in range(3):
        varfunc()


# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5

    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()
