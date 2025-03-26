from itertools import *

#zad4
"""
Korišdenjem programskog jezika Python, napisati funkciju zbir, koja kreira novu listu čiji su
elementi zbirovi susednih elementa liste.
Primer: zbir([1, 2, 3, 4, 5]) = [3, 5, 7, 9]
"""

def zbir(lista):
    return [lista[i]+lista[i+1] for i in range(len(lista)-1)]
print(zbir([1, 2, 3, 4, 5]))

