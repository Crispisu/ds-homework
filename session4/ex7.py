"""
    Ex. 7: Scrieti o functie care sa primeasca trei parametri
        - prefix (string)
        - word (string)
        - suffix (string)
    Si trebuie sa intoarca cuvantul cu prefixul si sufixul adaugate.

    Raspuns:
        - pentru prefix = 'a', suffix = 'b' si word = 'x'
            ---> 'axb'

    Observatii:
        - functia trebuie sa aiba MAXIM 1 linie de cod ca si body
"""

from typing_extensions import Concatenate


x = input("Introdu un prefix:")
y = input("Introdu cuvantul:")
z = input("Introdu si un sufix:")

def cuvant_nou (prefix, cuvant, sufix):
    return (prefix + cuvant + sufix)

print(cuvant_nou(x,y,z))