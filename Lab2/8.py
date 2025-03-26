from itertools import *
from functools import reduce
import operator
from re import *


#zad8
"""
Korišdenjem programskog jezika Python, napisati funkciju izracunaj, koja u listi koja može da se sastoji od
brojeva i podlisti, na n-tom mestu u rezultujudem nizu upisuje broj sa n-te pozicije iz ulaznog niza, a ukoliko se
radi o podlisti, zamenjuje je proizvodom svih brojeva u podlisti. Zabranjeno je korišdenje petlji (osim u
comprehension sintaksi).
Primer: izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]) = [1, 5, 15, 8, 2, 18]
"""

def izracunaj(lista):
    return list(map(lambda x: x if type(x)==int else reduce(lambda y, z: y*z, x, 1) ,lista))
print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))
