from itertools import *

#zad1
"""
Korišdenjem programskog jezika Python, napisati funkciju parni, koja listu brojeva
transformiše u rečnik parnih i neparnih brojeva.
Primer: parni([1, 7, 2, 4, 5]) = {'Parni': [2, 4], 'Neparni': [1, 7, 5]}
"""

def parni(lista):
    return {'Parni': [x for x in lista if x%2==0], 'Neparni': [x for x in lista if not x%2==0]}
print(parni([1, 7, 2, 4, 5]))
