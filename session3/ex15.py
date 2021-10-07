"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x = input()
vocale = "aeiou"
count = 0
for i in range (0,len(x)):
    if x[i] in vocale:
        count = count + 1
    
print (count)