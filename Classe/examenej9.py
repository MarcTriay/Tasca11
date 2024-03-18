#Crear una llista dels 10 primers números elevats a una potència donada. 
#Utilitzar list comprehensions. 
#Ex: Si volem el quadrat dels números de la llista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ,
#retorni [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], si la volem del cub retorni [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
#així successivament.

def num_elevats(b):
    c = [x**b for x in range(1,10)]
    print("EL nombre que volias elevar era {} i els resultats dels 10 primeres elevacions són: {}".format(b, c))


#P.Principal

b = int(input("Introdueix un numero: "))
num_elevats(b)