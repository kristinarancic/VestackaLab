from itertools import *

#zad6
"""
Korišdenjem programskog jezika Python, napisati funkciju razlika, koja prihvata dve liste
(bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih
elemenata iz prve liste, koji se ne nalaze u drugoj listi.
Primer: razlika([1, 4, 6, "2", "6"], [4, 5, "2"]) = [1, 6, "6"]
"""

def razlika(lista1, lista2):
    return list(filter(lambda x: x not in lista2, lista1))
print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))

