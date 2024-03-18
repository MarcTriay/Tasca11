def pot(p):
    r=[x**p for x in range(1,10)]
    print("Les potències elevades a {} dels 10 primers números és  {}".format(p,r))

#P.Principal
p=int(input("Introdueixi un numero al qual voleu elevar la resta: "))
pot(p)