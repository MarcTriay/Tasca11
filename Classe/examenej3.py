#Crear una funció que donada una llista de paraules i una lletra,
#retorni una llista amb les paraules que comencen per la lletra donada. Utilitzar filter. 
#Ex: [“maria”, “manta”, “peu”, “mà”] i li deim que ens retorni totes les que comencen per ‘p’, en retorni [‘peu’].

def llista(a):
    b = list(filter(lambda x: x[0] == "m" and x[1] == "a,", a))
    print(b)

#P.Principal
a = ["maria", "manta", "peu", "mà"]

llista(a)



