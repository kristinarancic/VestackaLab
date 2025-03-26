from itertools import *

#zad18
"""
Korišdenjem programskog jezika Python, napisati funkciju kreiraj, koja na osnovu ulazne
liste čiji su elementi podliste, kreira listu u kojoj svaki element rezultujude liste predstavlja
podlistu koja je razlika susednih podlisti ulazne liste.
Primer: kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]) =
 [[1, 3], [2], [4, 6, 7]]
"""

def kreiraj(lista):
    #return list(map(lambda x: list(filter(lambda y: y[0] not in y[1], x)) , pairwise(lista)))
    return [list(filter(lambda x: x not in lista[i+1], lista[i])) for i in range(len(lista)-1)]
print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))
