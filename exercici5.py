def crear_diccionari(l):
    d = dict()
    for i,e in enumerate(l):
        d[e]=i
    print("De la llista {} hem creat el diccionari {}".format(l,d))

#Programa principal
l= ['casa','cotxe','cadira','taula']
d = crear_diccionari(l)