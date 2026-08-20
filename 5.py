def procesar_coleccion(lista, transformar, filtrar):

    resultado = []

    for numero in lista:

        if filtrar(numero):

            nuevo = transformar(numero)

            resultado.append(nuevo)

    return resultado


def es_par(numero):
    return numero % 2 == 0


def duplicar(numero):
    return numero * 2


numeros = [1, 2, 3, 4, 5, 6]

print(
    procesar_coleccion(
        numeros,
        duplicar,
        es_par
    )
)
