"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""
import random
import string

# file = open("output17.data","x")

def dec(func):
    def wrapper (number):
        f = open("output17.data", "a")
        f.write(func(number) + '\n')
        f.close()
    return wrapper

@dec
def func(x):
    mystr = string.ascii_lowercase
    result = ''.join(random.choice(mystr) for i in range (x))
    print(result)
    return result

func(6)




