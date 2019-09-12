import random
#def generador(minimo,maximo):#
    #return random.randint(minimo,maximo)#

def generador_mejor(minimo,maximo,lista):
    encontrado = True
    while encontrado:
        aleatorio = random.randint(minimo,maximo)
        #encontrado = aleatorio in lista (resume todas las lineas de abajo#
        encontrado = False
        if aleatorio in lista:
            encontrado = True
    return aleatorio

if __name__=="__main__":
    print(generador_mejor(1,100,[ ]))
