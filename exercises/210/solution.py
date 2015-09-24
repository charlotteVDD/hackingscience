# -*- coding: utf-8 -*-
"""

@author: CharlotteVDD
"""
import is_prime

liste = range(1000)
result = 0
for i in range(1000):
    is_prime.is_prime(i)
    result = result + i
print(i)
