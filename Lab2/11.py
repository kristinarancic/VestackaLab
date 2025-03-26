from itertools import *
from functools import reduce
import operator
from re import *


#zad11
"""
Korišdenjem programskog jezika Python, napisati funkciju proizvod, koja vrada proizvod svih elemenata u listi
brojeva i svim njenim podlistama. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi) i funkcije
prod.
Primer: proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]]) = 4320

"""
def proizvod(lista):
    return reduce(lambda acc, x: acc*x if type(x)==int else acc*proizvod(x) ,lista, 1)
print(proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]]))
