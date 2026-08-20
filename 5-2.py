def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):

    if nombre_tarea != "":

        resultado = "Tarea realizada"

        if al_exito:
            al_exito(nombre_tarea, resultado)

    else:

        if al_error:
            al_error(nombre_tarea, "Error")


def exito(nombre, resultado):
    print(nombre, resultado)


def error(nombre, mensaje):
    print(nombre, mensaje)


ejecutar_mision(
    "Mi tarea",
    exito,
    error
)
