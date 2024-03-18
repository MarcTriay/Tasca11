#Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent.
#Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. Ex: def Passar_a_Numero(llista):
#retorni el número que corresponen els dígits.
from functools import reduce
def passar(llista):
    a = list(map(lambda x: str (x), llista))
    b = reduce(lambda x,y: x+y,a)
    print(b)

#P.Principal

llista = [3, 4, 1, 5]
passar(llista)
