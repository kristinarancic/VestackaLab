from itertools import *
from functools import reduce
import operator
from re import *

#zad12
"""
Korišdenjem programskog jezika Python, napisati funkciju izracunaj, koja u listi koja se sastoji od brojeva i
podlisti, menja svaki broj njegovim kvadratom, dok listu zamenjuje zbirom kvadrata brojeva koji je čine.
Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
Primer: izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]) = [4, 16, 14, 20, 4, 106]
"""

def izracunaj(lista):
    return list(map(lambda x: x*x if type(x)==int else reduce(lambda acc,y: acc+y*y ,x, 0) ,lista))
print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))
