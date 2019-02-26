#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-02-26 22:00:33
@LastEditTime: 2019-02-26 22:12:49
'''
import datetime

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyy。更多选项可以查看 strftime()方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthData = datetime.date(1941, 1, 5)

    print(miyazakiBirthData.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthData + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiBirthday = miyazakiBirthData.replace(year=miyazakiBirthData.year + 1)

    print(miyazakiBirthday.strftime('%d/%m/%Y'))
