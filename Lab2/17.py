from itertools import *
from functools import reduce
import operator
from re import *

#zad17
"""
Korišdenjem programskog jezika Python, napisati funkciju tekst, koja karaktere u tekstu koji su van
opsega malih, velikih slova i cifara (65-90 velika i 97-122 mala slova, 48-57 cifre), zamenjuje unicode
vrednošdu \ubbbb, gde bbbb predstavlja četvorocifrenu unicode reprezentaciju slova koje se
menja. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi).
Napomena: Za preuzimanje unicode reprezentacije slova mogude je koristiti funkciju ord, dok se za upisivanje
određenog broja nula ispred broja koristi funkcija zfill(brojNula). Prevođenje broja iz dekadnog u
heksadekadni se vrši korišdenjem funkcije hex.
Primer: tekst("Otpornost 10Ω.") = 'Otpornost\\u002010\\u03A9\\u002E'
"""

def tekst(text):
    return reduce(
        lambda acc, c: acc + (c if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9' else f"\\u{ord(c):04X}"),
        text,
        ''
    )
print(tekst("Otpornost 10Ω."))