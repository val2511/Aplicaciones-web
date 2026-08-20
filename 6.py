def buscar_clave_profunda(datos, clave):

    for nombre in datos:

        if nombre == clave:
            return datos[nombre]

        if type(datos[nombre]) == dict:

            resultado = buscar_clave_profunda(
                datos[nombre],
                clave
            )

            if resultado != None:
                return resultado

    return None


datos = {
    "persona": {
        "nombre": "Carlos",
        "ciudad": "Bogotá"
    }
}


print(buscar_clave_profunda(datos, "ciudad"))
