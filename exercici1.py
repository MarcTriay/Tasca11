def lenp(frase):
    b = frase.split(" ")
    c = list(map(len, b))
    print("La frase {} te les seguents logituds {}".format(frase, c))

#P.principal
frase =input("Introdueix una frase: ")
lenp (frase)