from itertools import *
from functools import reduce
import operator
from re import *

#zad5
"""
Korišdenjem programskog jezika Python, napisati funkciju proizvod, koja računa proizvod liste podlisti (A) i
liste brojeva (B). Smatrati da je broj podlisti u listi A jednak dužini liste B. Funkcija vrada listu koja ima onoliko
elemenata koliko je dužina ulaznih listi. N-ti element izlazne liste predstavlja sumu svih elemenata N-te
podliste liste A koji u prethodno pomnoženi N-tim elementom u liste B. Zabranjeno je korišdenje petlji (osim u
comprehension sintaksi) i funkcije sum.
Primer: proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]) = [6, 30, 72]
"""

def proizvod(lista1, lista2):
    return list(map(lambda x, y: reduce(lambda u, z: u+z, x)*y , lista1, lista2))
print(proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]))
