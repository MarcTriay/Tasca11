#Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem. 
#Utilitzar map. Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase.

def longitud(b):
    a = b.split(" ")
    c = list(map(len, a))
    print("La frase {} te les seguents logituds {}".format(b, c))

#P.Principal
b=input("Introdueix una frase: ")
longitud(b)