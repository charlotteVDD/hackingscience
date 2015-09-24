# -*- coding: utf-8 -*-
"""
You'll expose a perfect_shuffle(deck) function, perfectly shuffling
the given iterable.
@author: CharlotteVDD
"""
import itertools
import random


def perfect_shuffle(deck):
    random.shuffle(deck)
    return(deck)

liste = list(itertools.product(range(10)))
#print(liste)
tot = []
for i in range(10):
    random.shuffle(liste)
    tot.append(liste)
#print(tot)

# print(perfect_shuffle(liste))
