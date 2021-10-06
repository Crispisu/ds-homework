"""
    Ex. 2: Modificati urmatoarea bucata de cod astfel incat
    la rulare, rezultatul afisarii sa fie cele 2 liste concatenate.
    HINT: Exista mai multe moduri prin care puteti face asta.
"""
# Ii dam variabilei l1 ca si valoare o lista cu 4 elemente (1,2,3,4)
# si variabilei l2 ca valoare o lista cu 4 elemente (5,6,7)
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]
l3 = l1 + l2

# Afisam listele l1 si l2 separat.
# Pentru a vedea rezultatul, rulati acest script.
print(l1)
print(l2)
print(l3)
# sau, mai simplu, direct:
print (l1+l2)

# sau, mai dragut, asa:

l1.extend(l2)
print(l1)

# Sunt corecte cele 3 metode?