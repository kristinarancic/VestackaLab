from itertools import *

#zad13
"""
Korišdenjem programskog jezika Python, napisati funkciju izmeni, koja elemente na
parnim pozicijama uvedava za jedan i od njih kreira podlistu pp, dok elemente na
neparnim pozicijama umanjuje za 1 i od njih kreira podlistu np. Funkcija vrada rečnik koji
sadrži liste pp i np.
Primer: izmeni([8, 6, 3, 1, 1]) = {'pp': [9, 4, 2], 'np': [5, 0]}
"""

def izmeni(lista):
    return {'pp': [lista[i]+1 for i in range(len(lista)) if i%2==0], 'np': [lista[i]-1 for i in range(len(lista)) if i%2!=0]}
print(izmeni([8, 6, 3, 1, 1]))
