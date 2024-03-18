def filtrar(llista,c):
    l=list(filter(lambda x: x[0]==c.lower() or x[0]==c.upper(), llista))
    print("De la llista {}, les paraules que comencen per {} són {}".format(llista,c,l))

#P.Principal
llista =["maria", "manta", "peu", "mà"]
c= "p"
filtrar(llista,c)