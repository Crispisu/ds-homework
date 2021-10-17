"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""

def dec(func):
    def wrapper():
        x = func()
        print(x.upper())
    return wrapper


# decoarate me
@dec
def f():
    return 'cmi'

f()