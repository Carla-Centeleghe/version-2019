from competencia import generador_mejor
aleatorio = generador_mejor(1,100,[])
nadieadivino = False
while nadieadivino == False:
    print("ingrese un num entre 1 y 100")
    numero = int(input())
    if numero == aleatorio: 
        print("has adivinado")
        nadieadivino = True
    if numero<aleatorio:
        print(" mas grande")
    if numero>aleatorio:
        print("mas chico")
    if nadieadivino == False:
        numero = generador_mejor(1,100,[])
        print ("el numero pensado es "+ str(numero))
        if numero == aleatorio: 
            print("has adivinado")
            nadieadivino = True
        if numero<aleatorio:
            print(" mas grande computadora")
            lista = [numero]
        if numero>aleatorio:
            print("mas chico computadora")
            lista = [numero]
