from itertools import *
from functools import reduce
import operator
from re import *

#zad13
"""
Korišdenjem programskog jezika Python, napisati funkciju skupi, koja kreira novu listu tako da svaka dva
susedna elementa liste ciji su elementi iskljucivo podliste zamenjuje podlistom koja sadrži zbir elemeata na
odgovarajudim pozicijama. Elemente koji nedostaju tretirati kao nule. Zabranjeno je korišdenje petlji (osim u
comprehension sintaksi).
Primer: skupi([[1, 3, 5], [2, 4, 6], [1, 2]]) = [[3, 7, 11], [3, 6, 6]]
"""

def skupi(lista):
    #return list(starmap(lambda x,y: list(map(lambda u: u[0]+u[1] , zip_longest(x, y, 0))) , pairwise(lista)))
    return [[y+z for y, z in zip_longest(x[0], x[1], fillvalue=0)] for x in pairwise(lista)]
print(skupi([[1, 3, 5], [2, 4, 6], [1, 2]]))
