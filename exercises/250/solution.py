# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:58:34 2015

@author: CharlotteVDD
"""


def draw_n_square(n):
    for i in range(n):
        print((n * "+---") + "+", end=None)
        print((n + 1) * "|   ")
    print((n * "+---") + "+", end=None)
