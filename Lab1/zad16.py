from itertools import *

#zad16
"""
Korišdenjem programskog jezika Python, napisati funkciju brojanje, koja na osnovu datog
rečnika koji sadrži elemente različitog tipa kreira listu tuple objekata. Svaki tuple objekat
na prvoj poziciji sadrži tip elementa a na drugoj koliko je takvih elemenata bilo u rečniku.
Primer: brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}) =
[('int', 3), ('list', 2), ('str',1)]
"""

def brojanje(d):
    return [(tip, sum(1 for v in d.values() if type(v).__name__ == tip)) for tip in {type(v).__name__ for v in d.values()}]
print(brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}))
