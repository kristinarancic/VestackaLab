from itertools import *

#zad20
"""
Korišdenjem programskog jezika Python, napisati funkciju boje, koja RGB heksadekadni
zapis boje deli po kanalima i vrada rečnik sa odgovarajudim vrednostima u dekadnom
formatu.
Napomena: int("Broj u bazi N", N) može da se koristi za prevođenje iz baze N u bazu 10.
Primer: boje("#FA1AA0") = { "Red": 250, "Green": 26, "Blue": 160 }
"""

def boje(hex_kod):
   return dict(zip(["Red", "Green", "Blue"], map(lambda x: int(hex_kod[x:x+2], 16), [1, 3, 5])))

print(boje("#FA1AA0"))