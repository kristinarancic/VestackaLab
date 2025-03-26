from itertools import *
from functools import reduce
import operator
from re import *

#zad10
"""
Korišdenjem programskog jezika Python, napisati funkciju stepen, koja svaki par dva broja u ulaznoj listi (x, y),
transformiše u xy. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
Primer: stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]) = [1, 25, 64, 6, 1, 216, 9, 512]
"""

def stepen(lista):
    return list(map(lambda x: x[0]**x[1] ,pairwise(lista)))
print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))
