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

#Ejercicio 1 — Mostrar todos los nombres
'''
for i in alumno:
    print(i["nombre"])

#Ejercicio 2 Mostrar nombres y un valor numérico
for i in alumno:
    print(f"{i['nombre']} tiene un {i['nota']}")
'''
#5 mayor y menor
def MayorMenor():
    mayor =0
    menor = 9999
    nomMayor = ""
    nomMenor = ""

    for i in alumno:
        if i['nota']> mayor:
            mayor = i['nota']
            nomMayor = i['nombre']
        if i['nota']< menor:
            menor = i['nota']
            nomMenor = i['nombre']
    
    print(f"El mayor es {nomMayor} con una nota{mayor} ")
    print(f"El menor es  {nomMenor} con una nota{menor} ")
    
#6

def FiltrarPorNota():
    tuNota = int(input("Introduce tu nota "))
    simplificada =  []

    for i in alumno:
        if tuNota < i['nota']:
            print(i)


#8 Valor contextual

def ValorContextual():
        print("")


