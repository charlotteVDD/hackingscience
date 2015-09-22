# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
prints every possible combination of two letters,
only lower case, one by line, ordered alphabetically.
"""
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
R = len(alph)
print(R)
pairs = []
i = 0
for l in range(R):
    for k in range(R):
        if alph[l] != alph[k]:
            a = alph[l] + alph[k]
            b = alph[k] + alph[l]
            pairs.append(a)
            P = len(pairs)
            if b != pairs[i]:
                print(b)
                i = i + 1
        else:
            continue
