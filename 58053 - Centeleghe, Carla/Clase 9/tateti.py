from crucigrama import draw_tablero, full, win, validate 
#draw_tablero([" ", " ", " ", "  ", " ", "  ", " ", "  ", " "])
tablero = []
numeros=[]
for i in range(0,9):
    tablero.append(" ")
    numeros.append(str(i+1))
draw_tablero(numeros)
while  win(tablero) == False and  full(tablero) == False: 
    valido = False
    while not valido:
        print ("Es tu turno X, ingrese una posicion valida de 1 a 9")
        posicion = int(input())
        valido = validate (tablero,posicion)
        if not valido:
            print("Error de posicion")
    #numeros[posicion - 1] = "x"
    tablero[posicion - 1] = numeros[posicion - 1]= "x"
    draw_tablero(numeros)
   # gano = win(numeros)
    gano = win(tablero)
    if gano:
        print("Gano X")
    else:
        valido = False
        while not valido:
             print ("Es tu turno O, ingrese una posicion valida de 1 a 9")
             posicion = int(input())
             valido = validate (tablero,posicion)
             if not valido:
                 print("Error de posicion")
        #numeros[posicion - 1] = "o"
        tablero[posicion - 1] = numeros[posicion - 1]= "o"
        draw_tablero(numeros)
        #gano = win(numeros)
        gano = win(tablero)
        if gano:
             print("Gano O")
#if full(numeros) and not win(numeros):
if full(tablero) and not win(tablero):
    print("Nadie gano")
