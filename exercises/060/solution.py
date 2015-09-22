# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
prints every possible pairs of two letters,
only lower case, one by line, ordered alphabetically.
"""
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for l in range(26):
    for k in range(26):
        print(alph[l] + alph[k])
    
"""
s = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        s = s + i
print(s)
"""
