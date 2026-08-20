def aplanar_lista(lista):

    nueva_lista = []

    for elemento in lista:

        if type(elemento) == list:

            resultado = aplanar_lista(elemento)

            nueva_lista.extend(resultado)

        else:

            nueva_lista.append(elemento)

    return nueva_lista


lista = [1, [2, [3, 4], 5], 6, [7]]

print(aplanar_lista(lista))
