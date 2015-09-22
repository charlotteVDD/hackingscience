# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
prints the sum of every even numbers in the range [0; 100]"""
n = 0
for i in range(101):
    if i % 2 == 0:
        n = n + i
print(n)
