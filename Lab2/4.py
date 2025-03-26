from itertools import *
from functools import reduce
import operator
from re import *

#zad4
"""
Korišdenjem programskog jezika Python, napisati funkciju suma, koja vrada sumu svih elemenata u listi brojeva
i svim njenim podlistama. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi) i funkcije sum.
Primer: suma([[1, 2, 3], [4, 5, 6], [7, 8, 9], [5,5]]) = 45
"""

def suma(lista):
    return reduce(lambda acc, x: acc+x if type(x)==int else acc+suma(x) , lista, 0)
print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9], 5]))
