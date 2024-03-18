def nombre_posició(llista):
    l = []
    for i,e in enumerate(llista):
        if e == i:
            l.append(e)
        print ("El número de la llista \n{} \n que coincideixen en la posició són\n{}".format(llista,l))

#Programa principal
l=[1, 1, 2, 3, 7, 4, 7, 8, 10, 10]
nombre_posició(l)
