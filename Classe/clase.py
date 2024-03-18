def llegir_llista1():
    b=[]
    a='3'
    while a!='.':
        a = input("Introdueix un número per posar a la llista. ")
        if a!='.':
            b.append(int(a))
        else:
            return b
def suma(x,y):
    sumatori=0
    for e in x:
        sumatori+= e
    return sumatori
    
a = llegir_llista1()
b = llegir_llista1()
x = len(a)
y = len(b)
z = abs (x-y)
c = suma(a)
d = suma(b)
e = c + d