#Crear una funció que donada una llista, retorni un diccionari que tingui com a clau:
#els valors de la llista i com a valor el seu índex dins la llista. Utilitzar enumerate.
#Ex: (‘casa’,’cotxe’,’cadira’,’taula’) retorni {‘casa’:0, ‘cotxe’:1, ‘cadira’:2, ‘taula’:3}.

def llista(b):
    a = {}
    for i,e in enumerate (b):
        a[e] = i
    print("{}, {}".format(b,a))
#P.Principal
b = ("casa","cotxe","cadira","taula")
llista(b)
