"""
l=[3, 23, 73]
a=int(input("Hola: "))

x=list(map(lambda x: x*a, l))
print(x)

l= [2, 6, 54, 7]
a= int(input("Introdueix un numero: "))

p=list(filter(lambda x: x%2==0 ,l))
print("Aquest nombres son senars: {}".format(p))

#Retornar vocals 
c= "aixo es una prova:"
p=list(filter(lambda x: x in "aeiouAEIOUàáèéíòóú", c))
print(p)


#Funció reduce
from functools import reduce
m=[3,5,6]
s = reduce(lambda x,y: y+x , m)
print(s)

"""

l = [l,10,14, 654, 56]
x=reduce(lambda a,b: a.join (b), l)