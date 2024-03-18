#Crear una llista amb les lletres d’una paraula qualsevol. Utilitzar list comprehensions. 
#Ex: “institut”, retorni [‘i’,’n’,’s’,’t’,’i’,’t’,’u’,’t’].

def llista(a):
    b = [x for x in a]
    print("{} la hem transformat a {}".format(a, b))

#P.Principal

a= ["i","n","s","t","i","t","u","t"]
llista(a)