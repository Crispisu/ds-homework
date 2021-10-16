"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""
#file = open("output12.data","x")

def dec(func):
    def wrapper (valoare):
        f = open("output12.data", "w")
        f.write(valoare)
        f.close()
    return wrapper
    
# decorate me
@dec
def f(x):
    print(x)

f("jucarie")

file = open("output12.data","r")
print(file.read())
file.close()


