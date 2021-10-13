"""
    Ex. 3: Completati functia de mai jos, in asa fel incat sa intoarca
    o lista cu elementele pana la X (X fiind un parametru al functiei).

    Observatii:
        - X este un numar intreg (intotdeauna)
        - nu aveti voie sa folositi range()

    Rezultatul trebuie sa arate asa:
        - pentru x = 3 --> [0, 1, 2]
"""

def func(x):
    l = []
    while x > 0:
        l.insert(0,x-1)
        x = x-1
    return l

print(func(3))

#sau

def func2(x):
    l = []
    i = 0
    while i < x:
        l.append(i)
        i = i + 1
    return l

print(func2(3))

