from functools import reduce
def Passar_a_Numero(llista):
    a = list(map(lambda a:str(a), llista))
    b = reduce(lambda x,y:x+y,a)
    print("La llista {} es el numero {}".format(llista, b))

#P.Principal
a = [1, 3, 4, 5, 6]
Passar_a_Numero(a)