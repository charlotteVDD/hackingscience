# -*- coding: utf-8 -*-
"""

@author: CharlotteVDD
"""
import is_prime

liste = range(1000)
result = 0
prime = []
for i in range(1000):
    a = is_prime.is_prime(i)
    if a == True:
        result = result + i

print(result)
