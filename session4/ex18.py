"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""

def func(lista):
    lista = list(lista)
    if len(lista) == 1:
        return lista[0]
    element = lista[0]
    lista.pop(0)
    return element + func(lista)

print (func([1,2,3,4]))