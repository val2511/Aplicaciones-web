def crear_perfil_usuario(nombre, email, rol):

    if "@" not in email:
        return "Error en el correo"

    usuario = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }

    return usuario


print(crear_perfil_usuario(
    "Laura",
    "laura@empresa.com",
    "Desarrolladora"
))
