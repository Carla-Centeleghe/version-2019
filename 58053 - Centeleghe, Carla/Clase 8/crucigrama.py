def draw_tablero(tablero):
    print(' '+ tablero[0] + '  | ' + tablero[1] + '  | ' + tablero[2])
    print('____+____+____')
    print(' '+ tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('____+____+____')
    print(' '+ tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])
def validate(tablero, posicion):
    return tablero[posicion -1] == " "
def win(tablero):
    if tablero[0] != " " and tablero[0] == tablero[1] == tablero[2]:
        return True
    if tablero[3] != " " and tablero[3] == tablero[4] == tablero[5]:
        return True
    if tablero[6] != " " and tablero[6] == tablero[7] == tablero[8]:
        return True
    if tablero[0] != " " and tablero[0] == tablero[3] == tablero[6]:
        return True
    if tablero[1] != " " and tablero[1] == tablero[4] == tablero[7]:
        return True
    if tablero[2] != " " and tablero[2] == tablero[5] == tablero[8]:
        return True
    if tablero[0] != " " and tablero[0] == tablero[4] == tablero[8]:
        return True
    if tablero[2] != " " and tablero[2] == tablero[4] == tablero[6]:
        return True
    return False
