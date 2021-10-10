"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""




# asta l-am facut pwntru ca am gasit pe net cum sa faci random. se poate face si fara import?

from random import choice


x = input()
letters = 'abcdefghijklmnopqrstuvyz'
s = ''
for i in range (0, int(x)):
    s += choice(letters)

print(s)
