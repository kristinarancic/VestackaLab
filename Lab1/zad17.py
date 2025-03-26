from itertools import *

#zad17
"""
Korišdenjem programskog jezika Python, napisati funkciju kreiraj, koja kreira listu N tuple
obekata. Prvi element u svakom tuple objektu je redni broj tog tuple objekta a drugi
kvadrat zbira svih indeksa od 0 do trenutnog indeksa.
Primer: kreiraj(4) = [(0, 0), (1, 1), (2, 9), (3, 36), (4, 100)]
"""

def kreiraj(broj):
    return [(i, sum(range(i+1))**2) for i in range(broj+1)]
print(kreiraj(4))
