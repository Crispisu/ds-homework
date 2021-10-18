"""
    Ex. 16: Scrieti o functie upper care sa intoarca un text uppercase complet,
    primind un parametru my_str (string).
    --> f('cmi') --> 'CMI'

    Scrieti o functie lower care sa intoarca un text lowercase complet,
    primind un parametru my_str (string).
    --> f('CMI') --> 'cmi'

    Veti primi un input de la tastatura, un string.

    Scrieti o alta functie call_changers, care sa primeasca o functie ca si
    parametru, iar daca inputul are un numar par de caractere, va printa inputul
    cu uppercase, altfel, va printa inputut lowercase.

    Exemplu:
        - veti primi input: 'ceva'
            ---> CEVA
        - veti primi input: 'cEVa1'
            ---> ceva1
"""




# def call_changers(func):
#     x = input()
#     my_str = str(x)
#     if len(my_str) % 2 == 0:
#         def up_str(my_str):
#             return my_str.upper()
#     else:
#         def low_str(my_str):
#             return my_str.lower()
#     print(call_changers(x))

# x = input()
# my_str = str(x)
   
# def up_str(my_str):
#     return my_str.upper()
    
# def low_str(my_str):
#     return my_str.lower()

# def call_changers(func,x):
#     print(up_str(x)) if len(my_str) % 2 == 0 else print(low_str(x))

# call_changers(up_str(x),low_str(x))

x = input()
my_str = str(x)
   
def up_str(my_str):
    return my_str.upper()
    
def low_str(my_str):
    return my_str.lower()

def call_changers(func,my_str):
    print(func(my_str))

call_changers(up_str,my_str) if len(my_str) % 2 == 0 else call_changers(low_str,my_str)