from itertools import *
from functools import reduce
import operator
from re import *

#zad9
"""
Korišdenjem programskog jezika Python, napisati funkciju zamena, koja u listi brojeva, brojeve manje od broja
x, koji se prosleđuje kao argument, zamenjuje zbirom svih vrednosti ulazne liste, koje imaju indeks vedi od
indeksa broja koji se obrađuje. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
Primer: zamena([1, 7, 5, 4, 9, 1, 2, 7], 5) = [35, 7, 5, 19, 9, 9, 7, 7]
"""

def zamena(lista, vred):
    return [lista[i] if lista[i]>=vred else reduce(lambda x, y: x+y, lista[i+1:]) for i in range(len(lista))]
    #return list(map(lambda x: x if x>=vred else reduce(lambda y, z: y+z, lista[lista.index(x)+1:]) , lista))
print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))
