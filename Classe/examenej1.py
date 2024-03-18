#Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem. 
#Utilitzar map. Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase.

def lenp(frase):
    b = frase.split(" ")
    c = list(map(len,b))
    print("La frase {} te les seguents logituds {}".format(frase, c))
#P.Principal

frase=input("Introduzca una frase: ")
lenp (frase)