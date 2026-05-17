# problema1_hacer_sencillo.py
# Examen parcial #2 - Problema 1
# Algoritmo greedy para hacer sencillo con monedas {1, 5, 10, 25}.

def hacer_sencillo(monto_centavos):
    denominaciones = [25, 10, 5, 1]
    resultado = {}
    restante = monto_centavos

    for moneda in denominaciones:
        cantidad = restante // moneda
        resultado[moneda] = cantidad
        restante = restante % moneda

    return resultado


def contar_monedas(resultado):
    total = 0
    for moneda in resultado:
        total = total + resultado[moneda]
    return total


def imprimir_resultado(monto_centavos, resultado):
    print("Monto:", monto_centavos, "centavos")
    print("Q0.25:", resultado[25])
    print("Q0.10:", resultado[10])
    print("Q0.05:", resultado[5])
    print("Q0.01:", resultado[1])
    print("Total de monedas:", contar_monedas(resultado))
    print("-" * 35)


def ejecutar_pruebas():
    casos = [293, 87, 99]

    for monto in casos:
        resultado = hacer_sencillo(monto)
        imprimir_resultado(monto, resultado)


if __name__ == "__main__":
    ejecutar_pruebas()