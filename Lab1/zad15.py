from itertools import *

#zad15
"""
Korišdenjem programskog jezika Python, napisati funkciju izdvoji, koja iz zadate liste čiji su
elementi liste, izdvaja n-ti element i formira rezultujudu listu, pri čemu je n=0 za prvu
podlistu i uvedava se sukcesivno za 1. Ukoliko ne postoji n-ti element u listi vrada se 0.
Primer: izdvoji([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]) = [5, 9, 0, 12]
"""

def izdvoji(lista):
    return list(map(lambda x: x[lista.index(x)] if lista.index(x)<len(x) else 0 , lista))
print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))
