#!/usr/bin/env python
# coding=UTF-8
'''
@Description: About practicing python exercises
@Author: Shenhongwen
@LastEditors: Shenhongwen
@Date: 2019-03-21 20:37:47
@LastEditTime: 2019-03-21 20:50:29
'''
'''
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
'''
if __name__ == "__main__":
    import time
    import random
    play_it = input('do you wannt to play it.(\'y\' or \'n\')')
    while play_it == 'y':
        c = input('input a character to start:\n')
        i = random.randint(0, 2**32) % 100
        print('please input number you guess:\n')
        start = time.process_time()
        a = time.time()
        guess = int(input('input your guess:\n'))
        while guess != i:
            if guess > i:
                print('please input a little smaller')
                guess = int(input('input your guess:\n'))
            else:
                print('please input a little bigger')
                guess = int(input('input your guess:\n'))
        end = time.process_time()
        b = time.time()
        var = (end - start) // 18.2
        print(var)
        if var < 15:
            print(' you are very clever!')
        elif var < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
        print('Congradulations!')
        print('The number you guess is {:d}'.format(i))
        print(start)
        print(end)
        play_it = input('do you want to play it.')
