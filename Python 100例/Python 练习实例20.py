#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-27 21:20:27
@LastEditTime: 2019-02-27 21:25:31
'''


def ballfulldown():
    Msg = 'Well Done!'
    tour = []
    height = []
    hei = 100.0  # 起始高度
    tim = 10  # 次数
    for i in range(1, tim + 1):
        #  从第二次开始， 落地是的距离应该是反弹高度乘以2（弹到最高点再落下）
        if i == 1:
            tour.append(hei)
        else:
            tour.append(2*hei)
        hei /= 2
        height.append(hei)
    print('总高度：tour = {0}'.format(sum(tour)))
    print('第10次反弹高度: height = {0}'.format(height[-1]))
    return Msg


print(ballfulldown())
