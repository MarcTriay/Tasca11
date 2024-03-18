def llegir_llista1():
    a=[]
    for i in range (5):
        a.append(int(input(" ")))
    return a
def suma(x,y):
    c=[]
    for i in range (5):
        c.append(x[i]+y[i])
    print("La suma de les llistes a={} + b= {} és c= {}".format(x,y,c))

    
#P.Principal
a = llegir_llista1()
b = llegir_llista1()
suma(a, b)
