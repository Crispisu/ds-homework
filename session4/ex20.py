"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""
import json

# def read_from_file(file):
#     with open ('pisimic2.json') as file:
#         content = file.read()
#         print(content)

# read_from_file('pisimic2.json')

def read_from_file(filename):
    with open (filename) as file:
        content = file.read()
        dictionar = json.loads(content)
        print(dictionar)

read_from_file('pisimic2.json')