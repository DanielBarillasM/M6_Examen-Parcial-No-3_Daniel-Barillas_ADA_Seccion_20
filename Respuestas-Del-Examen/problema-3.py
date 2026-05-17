# problema3_nokia_dp.py
# Examen parcial #2 - Problema 3
# Programacion dinamica para contar combinaciones en teclado Nokia 3230.
#
# Para coincidir con el ejemplo del examen, se permite quedarse en la misma tecla.
# Movimientos validos: misma tecla, arriba, abajo, izquierda y derecha.

def construir_vecinos():
    teclado = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]
    ]

    movimientos = [
        [0, 0],    # misma tecla
        [-1, 0],   # arriba
        [1, 0],    # abajo
        [0, -1],   # izquierda
        [0, 1]     # derecha
    ]

    vecinos = {}

    for fila in range(len(teclado)):
        for columna in range(len(teclado[fila])):
            digito = teclado[fila][columna]

            if digito == "*" or digito == "#":
                continue

            vecinos[digito] = []

            for mov in movimientos:
                nueva_fila = fila + mov[0]
                nueva_columna = columna + mov[1]

                if nueva_fila < 0 or nueva_fila >= len(teclado):
                    continue

                if nueva_columna < 0 or nueva_columna >= len(teclado[nueva_fila]):
                    continue

                siguiente = teclado[nueva_fila][nueva_columna]

                if siguiente != "*" and siguiente != "#":
                    vecinos[digito].append(siguiente)

    return vecinos


def contar_combinaciones(n):
    if n <= 0:
        return 0

    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    vecinos = construir_vecinos()

    actual = {}
    for digito in digitos:
        actual[digito] = 1

    longitud = 2
    while longitud <= n:
        nuevo = {}
        for digito in digitos:
            nuevo[digito] = 0

        for origen in digitos:
            for destino in vecinos[origen]:
                nuevo[destino] = nuevo[destino] + actual[origen]

        actual = nuevo
        longitud = longitud + 1

    total = 0
    for digito in digitos:
        total = total + actual[digito]

    return total


def listar_combinaciones(n):
    # Funcion auxiliar para mostrar combinaciones cuando n es pequeno.
    # Para n grande, la lista crece rapidamente.
    if n <= 0:
        return []

    vecinos = construir_vecinos()
    combinaciones = []

    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for digito in digitos:
        combinaciones.append(digito)

    longitud = 2
    while longitud <= n:
        nuevas = []

        for combinacion in combinaciones:
            ultimo = combinacion[len(combinacion) - 1]

            for siguiente in vecinos[ultimo]:
                nuevas.append(combinacion + siguiente)

        combinaciones = nuevas
        longitud = longitud + 1

    return combinaciones


def ejecutar_pruebas():
    casos = [1, 2, 3, 5]

    for n in casos:
        total = contar_combinaciones(n)
        print("n =", n, "=> total de combinaciones:", total)

        if n == 2:
            combinaciones = listar_combinaciones(n)
            print("Primeras combinaciones para n = 2:")
            print(combinaciones[:20])

        print("-" * 45)


if __name__ == "__main__":
    ejecutar_pruebas()