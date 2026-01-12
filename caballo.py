MOVS_CABALLO = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]

estado = {"paso":0}

def es_valido(x, y, tablero):
    n = len(tablero)
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == 0

def pintar_recorrido(paso, tablero):
    print(f"Paso {paso}")
    for i in tablero:
        stringpaso = ""
        for j in i:
            stringpaso += f"{j:3d} "
        print(stringpaso)
    print()

def recorrido_caballo(tablero, x, y, paso):
    tablero[x][y] = paso

    if n*n == paso:
        return True
    
    for i in MOVS_CABALLO:
        movX = i[0]
        movY = i[1]
        if es_valido(x + movX, y + movY, tablero):
            if(recorrido_caballo(tablero, x + movX, y + movY, paso+1)):
                return True
    tablero[x][y] = 0
    


def resolver_recorrido(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    if recorrido_caballo(tablero, 0, 0, 1):
        print(f"recorrido encontrado en el tablero {n}x{n}")
        for i in tablero:
            stringpaso = ""
            for j in i:
                stringpaso += f"{j:3d} "
            print(stringpaso)
        print("Es un juego extraño, que tal si jugamos un tres en raya?")

n = 8
resolver_recorrido(n)