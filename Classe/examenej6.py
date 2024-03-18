#Crear una funció que donada una llista de valors numèrics,
#retorni el número d’elements on coincideix el valor i l’índex on és. Utilitzar enumerate.
#Ex: [0, 2, 3, 3, 4], retorni 3.

def llsiat(b):
    h = []
    for i,e in enumerate (b):
        if e==i:
            h.append(e)
    print(h)

#P.Principal
b = [1, 1, 4, 7, 4]
llsiat(b)