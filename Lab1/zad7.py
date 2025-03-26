from itertools import *
from functools import reduce

#zad7
"""
Korišdenjem programskog jezika Python, napisati funkciju saberi, koja listu tuple vrednosti
transformiše u listu brojeva, koji se dobijaju primenom operacije sabiranja.
Primer: operacija([(1, 4, 6), (2, 4), (4, 1)]) = [11, 6, 5]
"""

def saberi(lista):
    return list(map(lambda x: reduce(lambda y, z: y+z, x) , lista))
print(saberi([(1, 4, 6), (2, 4), (4, 1)]))
