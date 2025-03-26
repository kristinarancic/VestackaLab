from itertools import *
from functools import reduce
import operator
from re import *

#zad15
"""
Korišdenjem programskog jezika Python, napisati funkciju promeni, koja u listi brojeva, brojeve vede ili jednake
broju x, koji se prosleđuje kao argument, umanjuje za x, dok brojeve manje od x uvedava za x. Zabranjeno je
korišdenje petlji (osim u comprehension sintaksi).
Primer: promeni([7, 1, 3, 5, 6, 2], 3) = [4, 4, 6, 2, 3, 5]
"""

def promeni(lista, vred):
    return list(map(lambda x: x-vred if x>vred else x+vred ,lista))
print(promeni([7, 1, 3, 5, 6, 2], 3))
