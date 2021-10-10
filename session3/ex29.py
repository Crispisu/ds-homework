"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input()
vocale = "aeiou"
count = 0
count2 = 0

for i in range (0,len(x)):
    if x[i] in vocale:
        count = count + 1
    else:
        count2 = count2 + 1

print(count)
print(count2)

    