# -*- coding: utf-8 -*-
"""Created on Mon Sep 21 10:08:02 2015
@author: CharlotteVDD
prints every possible combination of two letters,
only lower case, one by line, ordered alphabetically.
"""
alph1 = "abcdefghijklmnopqrstuvwxyz"
alph2 = "abcdefghijklmnopqrstuvwxyz"
pairs = []
for i in range(len(alph1)):
    for j in range(i, len(alph2)):
        pair = alph1[i] + alph2[j]
        if alph1[i] != alph2[j]:
            pairs.append(pair)
        else:
            continue
for i in pairs:
    print(i)
