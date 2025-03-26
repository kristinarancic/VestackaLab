from itertools import *
from functools import reduce
import operator
from re import *

#zad2
"""
Korišdenjem programskog jezika Python, napisati funkciju spojidict, koja 2 liste obejkata objedinjuje u listu sa
elementima tipa dictionary. Dužina liste je dimenzija duže od dve ulazne liste. N-ti dictionary element
rezultujude kolekcije čine n-ti objekti iz obe ulazne liste, gde se na prvoj poziciji nalazi element prve liste
uparen sa ključem 'prvi', a na drugoj poziciji element druge liste uparen sa ključem 'drugi'. Kradu ulaznu
listu dopuniti sa '-', dok dužine obe liste ne budu iste. Zabranjeno je korišdenje petlji (osim u comprehension
sintaksi).
Primer: spojidict([1, 7, 2, 4], [2, 5, 2]) = [{'prvi': 1, 'drugi': 2},
{'prvi': 7, 'drugi': 5}, {'prvi': 2, 'drugi': 2}, {'prvi': 4, 'drugi': '-'}]
"""

def spojidict(lista1, lista2):
    return list(map(lambda x: {'prvi': x[0], 'drugi': x[1]} , zip_longest(lista1, lista2, fillvalue='-')))
print(spojidict([1, 7, 2, 4], [2, 5, 2]))
