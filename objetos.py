alumno = [
    {"nombre":"Dela", "edad":19, "nota":9.3, "Juego Favorito":"Oneshot", "deuda_publica":"Al menos 2"},
    {"nombre":"Guille", "edad":20, "nota":6.3, "Juego Favorito":"Destiny 2", "deuda_publica":"Sí"},
    {"nombre":"Iván", "edad":19, "nota":7.25, "Juego Favorito":"Dark Souls", "deuda_publica":"no se xd"},
    {"nombre":"Saif", "edad":19, "nota":9.75, "Juego Favorito":"Dark Souls 3", "deuda_publica":5},
    {"nombre":"Xinbo", "edad":19, "nota":9.3, "Juego Favorito":"Valorant", "deuda_publica":0},
    {"nombre":"Dani", "edad":23, "nota":8.0, "Juego Favorito":"Dispatch", "deuda_publica":0},
    {"nombre":"Gon", "edad":19, "nota":5.15, "Juego Favorito":"Celeste", "deuda_publica":"NaNeinf"},
    {"nombre":"Sara", "edad":20, "nota":6.3, "Juego Favorito":"Minecraft", "deuda_publica":3000000},
    {"nombre":"Ainoha", "edad":19, "nota":8.6, "Juego Favorito":"Animal Crossing", "deuda_publica":"0 (miente)"},
    {"nombre":"Patricia", "edad":19, "nota":6.25, "Juego Favorito":"Animal Crossing", "deuda_publica":"0 (miente)"},
    {"nombre":"Enrique", "edad":42, "nota":8.8, "Juego Favorito":"Mario Kart", "deuda_publica":"0 (miente)"}
]

edadActual = 19
media = 0
cuenta = 0
maxNota = ["nombre", 0]
minNota = ["nombre", 10]
lista = []

for clave in alumno:
    lista.append(clave["edad"])

moda = max(lista, key=lista.count)

for clave in alumno:
    print(f"Nombre: {clave["nombre"]}, Edad: {clave["edad"]}, Nota: {clave["nota"]}, Juego Favorito: {clave["Juego Favorito"]} Deuda pública: {clave["deuda_publica"]}")
    cuenta+=1
    media+=clave["edad"]
    if maxNota[1]<clave["nota"]:
        maxNota = [clave["nombre"], clave["nota"]]
    if minNota[1]>clave["nota"]:
        minNota = [clave["nombre"], clave["nota"]]

print("\n")
print(f"Media de edades: {int(media/cuenta)} \n")
print(f"Nota más grande: {maxNota} - Edad más pequeña: {minNota} \n")
print(f"Edad más repetida: {moda} \n")

filtro = int(input("Dame una edad para filtrar: "))
found = False
for clave in alumno:
    if clave["edad"] == filtro:
        found = True
        print(f"Nombre: {clave["nombre"]}, Edad: {clave["edad"]}, Nota: {clave["nota"]}, Juego Favorito: {clave["Juego Favorito"]} Deuda pública: {clave["deuda_publica"]}")

if found == False:
    print("Edad no encontrada.")