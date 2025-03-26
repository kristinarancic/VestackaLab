from itertools import *
from functools import reduce
import operator
from re import *

#zad18
"""
Korišdenjem programskog jezika Python, napisati funkciju brojevi, koja iz stringa izvlači listu svih
brojeva koji se u njemu nalaze. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
Primer: brojevi("42+10=52;10*10=100") = [ 42, 10, 52, 10, 10, 100 ]
"""

def brojevi(izraz):
    return list(map(lambda x: int(x) ,findall(r"\d+", izraz)))
print(brojevi("42+10=52;10*10=100"))