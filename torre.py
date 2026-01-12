torres = {
    "A":[3, 2, 1],
    "B":[],
    "C":[]
}

estado = {"paso":0}

print("\nProblema resuelto. Numero total de pasos:", estado["paso"])

def mover(torres, origen, destino):
    disco = torres[origen].pop()
    torres[destino].append(disco)

def dibujar_torres(torres, estado, origen, destino):
    print(f"paso: {estado}, mover disco de {origen} a {destino}")
    print("A: ", torres["A"])
    print("B: ", torres["B"])
    print("C: ", torres["C"])

def hanoi(n, origen, auxiliar, destino, torres, estado):
    if n==1:
        mover(torres, origen, destino)
        estado["paso"] += 1
        dibujar_torres(torres, estado["paso"], origen, destino)
        return
    
    hanoi(n-1, origen, destino, auxiliar, torres, estado)

    mover(torres, origen, destino)
    estado["paso"] += 1
    dibujar_torres(torres, estado["paso"], origen, destino)

    hanoi(n-1, auxiliar, origen, destino, torres, estado)


print("\nEstado inicial:")
print("A: ", torres["A"])
print("B: ", torres["B"])
print("C: ", torres["C"])

print("\nResolviendo...\n")
hanoi(3, "A", "B", "C", torres, estado)