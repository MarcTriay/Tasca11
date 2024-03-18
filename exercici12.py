import os

llista=["Jordi","Claudia","Sebas","Ian","Sergi","Alvaro", "Oscar","Marc","Anas","Fede", "Hugo", "Josep", "Fabri","Ayoub","Jose","David","Leiner","Clara","Paula"]
os.mkdir("home/cicles/AO/Tasca11/Prova")
os.chdir("/home/cicles/AO/Tasca11/Prova")
with open ("ex12.txt","w") as f:
    print+("Fitxer creat correctament")
    for e in llista:
        f.write(e+"\n")
professors=["David","Pep","Fela","Lluis","Joan"]
with open("ex12.txt","r") as f:
    for e in professors:
        f.write(e+"\n")
a= []
with open ("ex12.txt","r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print (a)
