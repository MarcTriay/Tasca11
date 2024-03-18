'''
with open ("/home/cicles/AO/Tasca11/fitxerpy.txt","a") as f:
    for i in range(4,11,):
        f.write(str(i)+"\n")
with open ("/home/cicles/AO/Tasca11/fitxerpy.txt","r") as f:
    a=0
    for line in f:
        if a%2==0:
            print(line)
        a+=1

import csv
with open ("/home/cicles/AO/Tasca11/prova.csv","a") as f:
    info = csv.reader(f)
    for linea in info:
        print(linea)

import json
dadesjson = '{"nom":"Joan","edad":45}' 
dades =json.loads(dadesjson)
print(dades)

import json
dades={"Nom":"Pere", "Cognom":"Pons", "Edat": 15}
with open("ex2.json", "w") as f: 
    json.dump(dades, f)
'''
#Mostraria la info de un pdf en internet a traves del enlace
from urllib import request
f = request.urlopen('https://core.ac.uk/download/pdf/52478597.pdf')
dades = f.read()
print(dades.decode('utf-8'))
