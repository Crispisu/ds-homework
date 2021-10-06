"""
    Ex. 7: Modificati urmatoarea bucata de cod astfel incat
    la rulare, la a doua afisare, in set sa existe si elementele din lista.
    Va veti folosi de lista, veti accesa elementele si le veti adauga in set.
"""

# In variabila s1 vom salva urmatorul set
s1 = {1, 2, 3}

# Cream variabila l1 ca o lista cu urmatoarele elemente:
l1 = [1, 4, 4, 5, 6]

# Afisam setul inainte de schimbare
print(s1)

# Adaugam valoarea 4 setului folosind metoda add()
s1.add(4)
s1.update (l1)
# Afisam setul dupa schimbare
print(s1)

# nu am inteles asta: Va veti folosi de lista, veti accesa elementele si le veti adauga in set
# am facut cum am stiut ca sa imi dea ce s-a cerut, dar partea de mai sus nu am inteles-o
