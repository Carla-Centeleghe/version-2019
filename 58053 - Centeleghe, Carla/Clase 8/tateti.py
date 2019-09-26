from crucigrama import draw_tablero, full, win, validate 
#draw_tablero([" ", " ", " ", "  ", " ", "  ", " ", "  ", " "])
tablero = []
for i in range(0,9):
    tablero.append(" ")
draw_tablero(tablero)
while  win(tablero) == False and  full(tablero) == False: 
    valido = False
    while not valido:
        print ("Es tu turno X, ingrese una posicion valida de 1 a 9")
        posicion = int(input())
        valido = validate (tablero,posicion)
        if not valido:
            print("Error de posicion")
    tablero[posicion - 1] = "x"
    draw_tablero(tablero)
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
        tablero[posicion - 1] = "o"
        draw_tablero(tablero)
        gano = win(tablero)
        if gano:
             print("Gano O")
if full(tablero) and not win(tablero):
    print("Nadie gano")
