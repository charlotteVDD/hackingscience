# -*- coding: utf-8 -*-
"""
You'll expose a perfect_shuffle(deck) function, perfectly shuffling
the given iterable.
@author: CharlotteVDD
"""
import itertools
import random


def perfect_shuffle(deck):
    pf = []
    n = len(deck)
    mid = int(n / 2)
    deck1 = list(itertools.islice(deck, mid - 1))
    deck2 = list(itertools.islice(deck, mid, n))
    for i in range(mid - 1):
        pf.append(deck1[i])
        pf.append(deck2[i])
    return(pf)
# liste = range(1024)
# perfect_shuffle(liste)
"""
    for i in n :
        pf.append(deck[i])
        pf.append(deck[i + 2])
    return(deck)

print perfect_shuffle()

liste = list(itertools.product(range(1024)))
# print(liste)
tot = []
for i in range():
    random.shuffle(liste)
    tot.append(liste)

# if tot[0] == tot[9]:
# print("perfect")
# print(tot)

# print(perfect_shuffle(liste))
"""