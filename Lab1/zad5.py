from itertools import *

#zad5
"""
Korišdenjem programskog jezika Python, napisati funkciju brojel, koja broji koliko
elemenata ima svaka podlista liste koja joj je prosleđena. Ukoliko elemenat liste nije
podlista funkcija vrada -1.
Primer: brojel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2]
"""

def brojel(lista):
    return list(map(lambda x: len(x) if type(x)==list else -1 , lista))
print(brojel([[1, 2], [3, 4, 5], 'el', ['1', 1]]))

