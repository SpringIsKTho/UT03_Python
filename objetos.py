alumno = [
    {"nombre":"Dela", "edad":19, "nota":9.3, "Juego Favorito":"Oneshot", "deuda_publica":"Al menos 2"},
    {"nombre":"Guille", "edad":20, "nota":6.3, "Juego Favorito":"Destiny 2", "deuda_publica":"Sí"},
    {"nombre":"Iván", "edad":20, "nota":7.25, "Juego Favorito":"Dark Souls", "deuda_publica":"no se xd"},
    {"nombre":"Saif", "edad":19, "nota":9.75, "Juego Favorito":"Dark Souls 3", "deuda_publica":5},
    {"nombre":"Xinbo", "edad":19, "nota":9.3, "Juego Favorito":"Valorant", "deuda_publica":0},
    {"nombre":"Dani", "edad":23, "nota":8.0, "Juego Favorito":"Dispatch", "deuda_publica":0},
    {"nombre":"Gon", "edad":19, "nota":5.15, "Juego Favorito":"Celeste", "deuda_publica":"NaNeinf"},
    {"nombre":"Sara", "edad":20, "nota":6.3, "Juego Favorito":"Minecraft", "deuda_publica":3000000},
    {"nombre":"Ainoha", "edad":19, "nota":8.6, "Juego Favorito":"Animal Crossing", "deuda_publica":"0 (miente)"},
    {"nombre":"Patricia", "edad":19, "nota":6.25, "Juego Favorito":"Animal Crossing", "deuda_publica":"0 (miente)"},
    {"nombre":"Enrique", "edad":42, "nota":8.8, "Juego Favorito":"Mario Kart", "deuda_publica":"0 (miente)"}
]

# Ejercicio 1 — Mostrar todos los nombres
for a in alumno:
    print(a["nombre"])

# Ejercicio 2 — Mostrar nombres y nota
for a in alumno:
    print(f"{a['nombre']} tiene un {a['nota']}")

# Ejercicio 5 — Mostrar alumno con mayor y menor nota
def MayorMenor(lista):
    mayor = lista[0]["nota"]
    menor = lista[0]["nota"]
    nomMayor = lista[0]["nombre"]
    nomMenor = lista[0]["nombre"]

    for a in lista:
        if a["nota"] > mayor:
            mayor = a["nota"]
            nomMayor = a["nombre"]
        if a["nota"] < menor:
            menor = a["nota"]
            nomMenor = a["nombre"]

    print(f"El mayor es {nomMayor} con una nota {mayor}")
    print(f"El menor es {nomMenor} con una nota {menor}")

MayorMenor(alumno)

# Ejercicio 6 — Filtrar alumnos con nota superior a un valor
def FiltrarPorNota(lista):
    valor = float(input("Introduce la nota mínima: "))

    for a in lista:
        if a["nota"] > valor:
            print(a)

FiltrarPorNota(alumno)

# Ejercicio 8 — Valor contextual (juego favorito más repetido)
def ValorContextual(lista):
    conteo_juegos = {}

    for a in lista:
        juego = a["Juego Favorito"]
        if juego in conteo_juegos:
            conteo_juegos[juego] += 1
        else:
            conteo_juegos[juego] = 1

    print(conteo_juegos)

ValorContextual(alumno)

# Ejercicio 9 — Crear lista con diccionarios simplificados
def NuevaLista(lista):
    nueva_lista = []

    for a in lista:
        nueva_lista.append({
            "nombre": a["nombre"],
            "edad": a["edad"]
        })

    print(nueva_lista)

NuevaLista(alumno)

# Ejercicio 12 — Ordenar por nota de mayor a menor
def OrdenarPorNota(lista):
    lista_ordenada = sorted(lista, key=lambda x: x["nota"], reverse=True)
    for a in lista_ordenada:
        print(f"{a['nombre']} tiene nota {a['nota']}")

OrdenarPorNota(alumno)

# Ejercicio 13 — Ordenar por edad de mayor a menor
def OrdenarPorEdad(lista):
    lista_ordenada = sorted(lista, key=lambda x: x["edad"], reverse=True)
    for a in lista_ordenada:
        print(f"{a['nombre']} tiene una edad de {a['edad']}")

OrdenarPorEdad(alumno)

# Ejercicio 15 — Actualizar un campo de un alumno
def ActualizarAlumno(lista):
    nombre_buscar = input("Introduce el nombre del alumno a actualizar: ")
    campo = input("Introduce el campo a modificar (edad, nota, Juego Favorito, deuda_publica): ")
    nuevo_valor = input("Introduce el nuevo valor: ")

    if campo == "edad":
        nuevo_valor = int(nuevo_valor)
    elif campo == "nota":
        nuevo_valor = float(nuevo_valor)

    for a in lista:
        if a["nombre"].lower() == nombre_buscar.lower():
            a[campo] = nuevo_valor
            print(f"{nombre_buscar} actualizado correctamente.")
            return

    print(f"No se encontró ningún alumno llamado {nombre_buscar}.")

# Ejercicio 16 — Eliminar alumno por nombre
def EliminarAlumno(lista):
    nombre_buscar = input("Introduce el nombre del alumno a eliminar: ")

    for i, a in enumerate(lista):
        if a["nombre"].lower() == nombre_buscar.lower():
            del lista[i]
            print(f"{nombre_buscar} eliminado correctamente.")
            return

    print(f"No se encontró ningún alumno llamado {nombre_buscar}.")

# Ejercicio 18 — Resumen de alumnos
def Resumen(lista):
    total = len(lista)
    suma_notas = 0
    max_nota = lista[0]["nota"]
    min_nota = lista[0]["nota"]
    juegos = {}

    for a in lista:
        suma_notas += a["nota"]

        if a["nota"] > max_nota:
            max_nota = a["nota"]
        if a["nota"] < min_nota:
            min_nota = a["nota"]

        juego = a["Juego Favorito"]
        if juego in juegos:
            juegos[juego] += 1
        else:
            juegos[juego] = 1

    media = suma_notas / total
    juego_mas_comun = max(juegos, key=juegos.get)

    print({
        "total_alumnos": total,
        "media_nota": media,
        "max_nota": max_nota,
        "min_nota": min_nota,
        "juego_mas_comun": juego_mas_comun
    })

Resumen(alumno)

# Ejercicio 20 — Exportar datos filtrados por nota
def ExportarFiltrados(lista):
    valor = float(input("Introduce la nota mínima: "))
    filtrados = []

    for a in lista:
        if a["nota"] > valor:
            filtrados.append({
                "nombre": a["nombre"],
                "nota": a["nota"]
            })

    print(filtrados)

ExportarFiltrados(alumno)

# Ejercicio 23 — Mostrar el Top N alumnos por nota
def TopN(lista):
    N = int(input("Introduce el número de alumnos: "))
    lista_ordenada = sorted(lista, key=lambda x: x["nota"], reverse=True)

    for a in lista_ordenada[:N]:
        print(f"{a['nombre']} con nota {a['nota']}")

TopN(alumno)
