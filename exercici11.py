def imprimir_fixer(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c= e.split("\n")
            if c!='':
                a.append(c[0])
    print(a)

def afegir_fitxer(m,llista):
    with open (m,"a+") as f:
        for e in llista:
            f.writelines(e+"\n")

#P.principal
fitxer = "/home/cicles/AO/Tasca11/exercici11.py"
llista=["Jordi","Claudia","Sebas","Ian","Sergi","Alvaro", "Oscar"]
afegir_fitxer(fitxer, llista)
imprimir_fixer(fitxer)
