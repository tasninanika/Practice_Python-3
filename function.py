# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:08:40 2025

@author: Jarin
"""

# static function
def gretting():
    print('Jarin Tasnin Anika')

gretting()


# dynamic function

def my_print(x):
    print(x)

my_print('Jarin')


# practice

def my_range(start_num, end_num, increment_num):
    while start_num <= end_num:
        print(start_num)
        start_num += 1

my_range(0, 20, 1)
    