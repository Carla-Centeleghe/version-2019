from generador import generador
adivinador = False
aleatorio = generador (1,20)

while adivinador == False:
    print(" ingrese un num entre 1 y 20")
    numero = int(input())
    if numero == aleatorio: 
        print("has adivinado")
        adivinado = True
    if numero<aleatorio:
        print(" mas grande")
    if numero>aleatorio:
        print("mas chico")