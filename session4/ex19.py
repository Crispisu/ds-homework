"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""

import random
import string 
import json


# def func(x):
#     x = str(x)
#     try:
#         file = open(x + '.json',"w")
#     except OSError:
#         file = open(x + '.json',"x")
#     finally:
#         file.write('{ \n')
#     for i in range (0,4):
#         key = random.randint(0,10)
#         alfabet = string.ascii_lowercase
#         string_len = random.randint(3,6)
#         value = ''.join(random.choice(alfabet) for i in range (string_len))
#         file.write('\t' + str(key) + ': \'' + value + '\' \n')
#     file.write('}')
#     file.close()

# func('pisimic')

def func(x):
    x = str(x)
    dictionar = {}
    try:
        file = open(x + '.json',"w")
    except OSError:
        file = open(x + '.json',"x")
    for i in range (0,4):
        key = random.randint(0,10)
        alfabet = string.ascii_lowercase
        string_len = random.randint(3,6)
        value = ''.join(random.choice(alfabet) for i in range (string_len))
        dictionar[key] = value
    dict = json.dumps(dictionar)
    file.write(dict)
    file.close()
    

func('pisimic2')