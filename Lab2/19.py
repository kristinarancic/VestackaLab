from itertools import *
from functools import reduce
import operator
from re import *

#zad19
"""
Korišdenjem programskog jezika Python, napisati funkciju brojanje, koja broji koliko karaktera se
ponavlja uzastopno više puta u prosleđenom stringu. Zabranjeno je korišdenje petlji (osim u
comprehension sintaksi).
Primer: izbaci("aatesttovi") = 2
"""

def brojanje(strUlaz):
    return reduce(lambda acc, b: acc+1 if b > 1 else acc, (starmap(lambda a, b: len(list(b)), groupby(strUlaz))), 0)
print(brojanje("aatesttovii"))
