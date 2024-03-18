def menu():
    opcio=1
    while opcio<1 or opcio >5:
        print("""
          Menu Principal:
          1. Programació estructurada
          2. Programació funcional
          3. Programació orientada a Objectes
          4. Acces a fitxers
          5. Sortir          
          """)
    opcio = int(input("Seleccioni l'opcii que vulgui executar: "))
    if opcio<1 or opcio >5:
        print("Opcio no valida")
    else:
        return opcio
def Programació_estructurada():
    print("Molt bé has entrat a la programació estructurada")
    l=["Pere","Pau", "Paula"]
    x=list(map(lambda x: len(x) >4,l))
    print(x)

def Programació_funcional():
    print("Molt bé has entrat a la programació funcional")


def Programació_orientada_a_Objectes():
    print("Molt bé has entrat a la programació orientada a objectes")

def Acces_a_fitxers():
    print("Molt bé has entrat al acces de fitxers")

#P.principal

op=1
while op!=5:
    match(op):
        case 1:
            Programació_estructurada()
        case 2:
            Programació_funcional()
        case 3:
            Programació_orientada_a_Objectes()
        case 4:
            Acces_a_fitxers()
        case 5:
            print("Gracies per utilitzar el programa")

menu()


