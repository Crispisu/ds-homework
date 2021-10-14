"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""

x = input()
t = "abcdefghijklmnopqrstuvwxyz"
litere = list(t)


def next_letter (string):
    s = ""
    for i in string:
        s = s + litere[litere.index(i)+1]
    return(s)

print(next_letter(x))


