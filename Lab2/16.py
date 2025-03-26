from itertools import *
from functools import reduce
import operator
from re import *

#zad16
"""
Korišdenjem programskog jezika Python, napisati funkciju broj, koja na osnovu heksadekadnog
broja koji predstavlja boju na ulazu u formatu #RGB, određuje integer reprezentaciju tog broja, koja
se dobija slededim obrascem: (R * 65536) + (G * 256) + B. Zabranjeno je korišdenje petlji (osim u
comprehension sintaksi).
Napomena: Broj N je mogude prevesti iz baze B u bazu 10 korišdenjem funkcije int(N, B)
Primer: broj("#FA0EA0") = 16387744
"""

def broj(hex_kod):
    return reduce(lambda acc, x: acc*256+int(hex_kod[x:x+2], 16) ,[1, 3, 5], 0)
print(broj("#FA0EA0"))
