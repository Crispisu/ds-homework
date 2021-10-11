"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
x = input()
l = []

for i in x:
    l.append(i)
try:
    for element in l:
        
        if element == "(":
            l.pop(l.index(")",l.index(element)))
            
        if element == "[":
            l.pop(l.index("]",l.index(element)))
            
        if element == "{":
            l.pop(l.index("}",l.index(element)))
            
            
except ValueError:
    print (False)
else:
    if l.count(")") > 0 or l.count("]") > 0 or l.count("}") > 0:
        print(False)
    else:
        print (True)

# else: (asta nu o mai folosim)

# x = input()
# r_d = 0
# r_i = 0
# p_d = 0
# p_i = 0
# a_d = 0
# a_i = 0

# for i in x:
#     if i == "(":
#         r_d += 1
#     if i == ")":
#         r_i += 1
#     if i == "[":
#         p_d += 1
#     if i == "]":
#         p_i += 1
#     if i == "{":
#         a_d += 1
#     if i == "}":
#         a_i += 1
# if r_d == r_i and p_d == p_i and a_d == a_i:
#     print(True)
# else: 
#     print(False)
    


        
        
    