# -*- coding: utf-8 -*-
"""
You'll expose a perfect_shuffle(deck) function, perfectly shuffling
the given iterable.
@author: CharlotteVDD
"""
import itertools


def perfect_shuffle(deck):
    pf = []
    n = len(deck)
    mid = int(n / 2)
    if len(deck) > 0:
        deck1 = list(itertools.islice(deck, mid - 1))
        deck2 = list(itertools.islice(deck, mid, n))
        for i in range(mid - 1):
            pf.append(deck1[i])
            print(pf)
            pf.append(deck2[i])
    return(pf)
