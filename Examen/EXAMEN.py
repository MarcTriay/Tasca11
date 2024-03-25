def menu():
    op = 0
    while op > 1 or op <14:
        print("""
        Programa Principal
        1. Estructures condicionals, if
        2. Estructures condicionals, match
        3. Estructures iteratives, for e in b
        4. Estructures iteratives, for e in range(x)
        5. Estructures iteratives, for i,e in enumerate(a)
        6. Funció amb parametres
        7. Funció Lambda
        8. Funció list comprhesion
        9. Funció map
        10. Funció zip
        11. Funció filter
        12. Fitxers
        13. Sortir        
        """)
        op = int(input("Introdueix una opció: "))
        if op <1 or op >14:
            print("Opció no valida, torni a elegir una opció \n")
        else:
            return op

def ex1():
    a = int(input("Introdueixi un numero: "))
    b = int(input("Introdueixi un altre numero: "))
    if a < b :
        print("{} és major que {}".format(b,a))
    elif a > b:
        print("{} és major que {}".format(a,b))
    else:
        print("{} g {} són iguals".format(a,b))
def ex2():
    vocal = input("introdueix una lletra: ")
    match(vocal):
        case "a":
            print("La vocal introduida és una a")
        case "e":
            print("La vocal és una e")
        case "i":
            print("La vocal és una i")
        case "o":
            print("La vocal és una o")
        case "u":
            print("La vocal és una u")
        case other:
            print("Opció no valida")
def ex3():
    a = []
    b = []
    for i in a:
        a.append(input("Introdueixi una paraula:"))
    for e in a:
        b.append(len(a))
    print("Les longituds de la llista {} sób {}".format(a,b))

def ex4():
    a = []
    for e in range (1,10,2):
            a.append(e)
            print("Dels 5 primers nombres, els impors són : {}".format(a))
def ex5():
    a = [1,2,3,4,5]
    dic = {}
    for i,e in enumerate(a):
        dic [i]=e
    print("De la llista{} hem creat el diccionari {}".format(a, dict))
def ex6(llista, a):
    b = []
    for e in llista:
        if a in e:
            b.append(e)
    print("La llista {} que conte la lletra {} son {}".format(llista,a,b))
def ex7():
    a = [2,6,8,20,32]
    c = list(map(lambda x: x+10,a))
    print(c)
def ex8():
    a = [2,6,3,4,8]
    r = [x**2 for x in a if x%2==1]
    print("EL quadrat dels numeros inàrs és{}".format)
def ex9():
    a= []
    c= list(map(lambda x : x [::-1],a))
    print(c)
def ex10():
   a = [1,2,3,4,5]
   b = [6,7,8,9,10]
   c = list(zip(a,b))
   print(c)
    
def ex11():
    a = [1,2,3,4,5]
    b = list(filter(lambda x: x%2==1,a))
    print(b)

class Ordinador():
    def __init__(self,tipus,pantalla):
        self.tipus=tipus
        self.pantalla = pantalla
        def getTipus (self):
            print(self.tipus)
        def getpantalla(self):
            print(self.pantalla)
class Portatil(Ordinador):
    def getTipus():
        print("SOc un portatil")
    def getPantalla():
        print("15")        
class Tablet(Ordinador):
    def getTipus():
        print("Soc una tablet")
    def getPantalla():
        print("9")
class Servidor(Ordinador):
    def getTipus():
        print("Soc un servidor")
    def getPantalla():
        print("21")
class PC(Ordinador):
    def getTipus():
        print("Soc un PC")
    def getPantalla():
        print("27")
def ex12():
    llista= [Portatil("portatil","15")],[Tablet("Soc una tablet","9")],[Servidor("Soc un servidor","21")],[PC("Soc un pc"),("27")]
    for e in llista:
        e.getTipus()
        e.getPantalla()
def ex13():
    with open("/home/cicles/AO/ex20.txt","w") as f:
        for e in range(10):
            f.write(str(e)+"\n")
    with open ("/home/cicles/AO/ex20.txt","r") as f:
        for e in f:
            print(e)       

#P.Principal
op= 1
while op!=14:
    op = menu()
    match(op):
        case 1:
            ex1()
        case 2:
            ex2()
        case 3:
            ex3()
        case 4:
            ex4()
        case 5:
            ex5()
        case 6:
            l = ["hola","adeu", "hello", "bye","alt", "baix"]
            c="a"
            ex6(l,c)
        case 7:
            ex7()
        case 8:
            ex8()
        case 9:
            ex9()
        case 10:
            ex10()
        case 11:
            ex11()
        case 12:
            ex12()
        case 13:
            ex13()
        case 14:
            print("Programa acabat, que ho passi molt bé i gràcies per utilitzar-me!")