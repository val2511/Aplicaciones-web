def calcular_metricas(*numeros, **opciones):

    operacion = opciones.get("operacion")

    if operacion == "suma":
        return sum(numeros)

    if operacion == "promedio":
        return sum(numeros) / len(numeros)


print(calcular_metricas(
    10, 20, 30,
    operacion="suma"
))
