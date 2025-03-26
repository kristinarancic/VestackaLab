from itertools import *

#zad2
"""
Korišdenjem programskog jezika Python, napisati funkciju numlista, koja iz liste koja može
da sadrži elemente različitog tipa izdvaja vrednosti po tipu i smešta ih u rečnik.
 Napomena: Naziv tipa može da se preuzme korišćenjem atributa __name__ nad samim tipom podataka.
Primer: numlista(["Prvi", "Drugi", 2, 4, [3, 5]]) =
 {'str': ["Prvi", "Drugi"], 'int': [2, 4], 'list': [[3, 5]]}
"""

def numlista(lista):
    return {type(x).__name__: [y for y in lista if type(y).__name__==type(x).__name__]  for x in lista}
print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))
