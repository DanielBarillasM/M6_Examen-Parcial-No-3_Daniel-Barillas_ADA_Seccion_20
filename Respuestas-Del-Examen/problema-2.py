# problema2_knapsack_fraccionado.py
# Examen parcial #2 - Problema 2
# Algoritmo greedy para knapsack fraccionado por unidades.

def knapsack_fraccionado(items, capacidad):
    # Cada item tiene la forma:
    # [nombre, precio_total, unidades_disponibles]
    items_con_valor_unitario = []

    for item in items:
        nombre = item[0]
        precio_total = item[1]
        unidades = item[2]
        valor_unitario = precio_total / unidades
        items_con_valor_unitario.append([nombre, precio_total, unidades, valor_unitario])

    items_ordenados = sorted(
        items_con_valor_unitario,
        key=lambda item: item[3],
        reverse=True
    )

    restante = capacidad
    valor_total = 0
    seleccion = []

    for item in items_ordenados:
        if restante == 0:
            break

        nombre = item[0]
        unidades_disponibles = item[2]
        valor_unitario = item[3]

        tomar = unidades_disponibles
        if tomar > restante:
            tomar = restante

        valor_tomado = tomar * valor_unitario
        valor_total = valor_total + valor_tomado
        restante = restante - tomar

        seleccion.append([nombre, tomar, valor_unitario, valor_tomado])

    return seleccion, valor_total


def imprimir_resultado(nombre_caso, items, capacidad):
    print(nombre_caso)
    print("Capacidad:", capacidad)
    print("Items:")
    for item in items:
        print(" ", item[0], "precio:", item[1], "unidades:", item[2])

    seleccion, valor_total = knapsack_fraccionado(items, capacidad)

    print("Seleccion:")
    for parte in seleccion:
        print(
            " ",
            parte[0],
            "unidades tomadas:",
            parte[1],
            "valor unitario:",
            round(parte[2], 4),
            "valor tomado:",
            round(parte[3], 4)
        )

    print("Valor total:", round(valor_total, 4))
    print("-" * 45)


def ejecutar_pruebas():
    items1 = [
        ["item 1", 60, 10],
        ["item 2", 100, 20],
        ["item 3", 120, 30]
    ]
    imprimir_resultado("Caso 1: ejemplo del examen", items1, 50)

    items2 = [
        ["oro", 40, 10],
        ["plata", 45, 15],
        ["bronce", 70, 20]
    ]
    imprimir_resultado("Caso 2: capacidad 15", items2, 15)

    items3 = [
        ["A", 10, 5],
        ["B", 24, 6],
        ["C", 12, 4]
    ]
    imprimir_resultado("Caso 3: capacidad 7", items3, 7)


if __name__ == "__main__":
    ejecutar_pruebas()