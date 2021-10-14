"""
    Ex. 5: Scrieti o functie cu un singur parametru (o lista) care sa
    adauge 1 tuturor elementelor din lista.

    Raspunsul corect:
        - func([1, 2, 3])
            ---> [2, 3, 4]

    Observatii:
        - functia trebuie sa fie MAXIM o linie de cod (2, daca luam in calcul
        si definitia functiei)
        - hint: list comprehensions (google it if you don't know it already)
"""
x = int(input())
l = [i + 1 for i in range(0,x)]


def adauga_1 (lista):
    print([elem + 1 for elem in lista])

adauga_1(l)

# si pt ca mai sus am avut impresia ca lista tb sa fie in baza unui input, ma pedepsesc eu pe mine si fac si varianta
# pe care ati cerut-o voi:

x = [5,6,7]

def adaugaunu (lista):
    print([n +1 for n in x])

adaugaunu(x)

    
