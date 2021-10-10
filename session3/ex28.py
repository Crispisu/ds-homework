"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
x = int(input())
s = 0
l = []

for i in range (1,x+1):
    l.append(i)
    s = sum(l)
    
print (s)

#sau:

x = int(input())
s = 0
for i in range (1,x+1):
    s = s + i
    
print (s)